import os
import psycopg2
from dotenv import load_dotenv
from pymongo import MongoClient  # Import MongoDB
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Application

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")  # MongoDB connection string

# Connect to MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["sportsfinder"]  # Use the database "sportsfinder"
users_collection = db["users"]  # Use the collection "users"

# Create the Telegram Bot application
application = Application.builder().token(TOKEN).build()

# Function to handle /start command
async def start(update: Update, context):
    user_telegram_id = update.message.from_user.id
    user_first_name = update.message.from_user.first_name or "Unknown"

    # Check if the user exists in MongoDB
    existing_user = users_collection.find_one({"chat_id": user_telegram_id})
    
    if not existing_user:
        # Insert user if they are new
        users_collection.insert_one({
            "chat_id": user_telegram_id,
            "name": user_first_name,
            "age": None,
            "gender": None,
            "sports": [],
            "location": None
        })
        welcome_message = f"Hello {user_first_name}, welcome to Sportsfinder! 🏆\n\n"
    else:
        welcome_message = f"Welcome back, {user_first_name}! 🎉\n\n"

    # Create the web app button
    keyboard = [[InlineKeyboardButton("My Profile", web_app={'url': 'https://barbaracwx.github.io/sportsfinder/'})]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_message + "Are you ready to find your sports partner?\n\nClick the button below to set up your profile.",
        reply_markup=reply_markup
    )

# Register the /start command handler
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Start the bot
application.run_polling()
