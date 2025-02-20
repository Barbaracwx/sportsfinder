import os
import psycopg2
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Application

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL") 

# Create the Telegram Bot application
application = Application.builder().token(TOKEN).build()

# Function to get a database connection
def get_db_connection():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

# Function to handle /start command
async def start(update: Update, context):
    user_telegram_id = update.message.from_user.id
    user_first_name = update.message.from_user.first_name or "Unknown"

    # Store user info in the database if chat_id does not exist
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (chat_id, name) VALUES (%s, %s) ON CONFLICT (chat_id) DO NOTHING",
            (user_telegram_id, user_first_name)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")

    # Send the welcome message with a web app button
    keyboard = [[InlineKeyboardButton("My Profile", web_app={'url': 'https://barbaracwx.github.io/sportsfinder/'})]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Hello {user_first_name}, welcome to Sportsfinder! 🏆\n\n"
        "Are you ready to find your sports partner?\n\n"
        "Click the button below to set up your profile.",
        reply_markup=reply_markup
    )

# Register the /start command handler
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Start the bot
application.run_polling()
