import os
import psycopg2
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Application

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# Create the Application object
application = Application.builder().token(TOKEN).build()

# Database connection
DATABASE_URL = os.getenv("postgres://u74paoavmds30r:pf5baba4878a23ad2fa9729b32256b75aa27c1aa49e4fad94e6243afd15ddfae1@c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d196r0fv8p6tii")
DATABASE_URL = os.getenv("DATABASE_URL") 
connection = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = connection.cursor()

# Print the current database to confirm the connection
cursor.execute("SELECT current_database();")
current_database = cursor.fetchone()
print(f"Connected to database: {current_database[0]}")

# Function to start the bot
async def start(update: Update, context):
    user_telegram_id = update.message.from_user.id
    user_first_name = update.message.from_user.first_name

    keyboard = [
        [
            InlineKeyboardButton(
                "My Profile",
                web_app={'url': 'https://barbaracwx.github.io/sportsfinder/'}
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Hello there, {user_first_name} and welcome to Sportsfinder!\n\n"
        "Are you ready to find your sports partner?\n\n"
        "Click the button below to set up your profile", 
        reply_markup=reply_markup
    )

# Function to register the user (store info in the database)
async def register(update: Update, context):
    chat_id = update.message.chat_id
    user_name = ' '.join(context.args)

    if user_name:
        try:
            # Insert user data into PostgreSQL database
            cursor.execute("INSERT INTO users (chat_id, name) VALUES (%s, %s) ON CONFLICT (chat_id) DO NOTHING", (chat_id, user_name))
            connection.commit()

            await update.message.reply_text(f"Hello {user_name}, you have been successfully registered!")
        except Exception as e:
            connection.rollback()
            print(f"Error occurred while inserting user data: {e}")
            await update.message.reply_text("There was an error while registering you. Please try again.")
    else:
        await update.message.reply_text("Please provide your name after the /register command. Example: /register John Doe")

# Register the /start and /register commands
start_handler = CommandHandler('start', start)
register_handler = CommandHandler('register', register)

# Add the handlers to the application
application.add_handler(start_handler)
application.add_handler(register_handler)

# Start the bot
application.run_polling()
