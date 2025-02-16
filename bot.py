from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler
import os
import psycopg2
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("7537818430:AAFOt1K8xnYUOedx5gaFgvPAkFKUwA9FIdk")
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
bot = Bot(TOKEN)

# Connect to PostgreSQL using the DATABASE_URL from Heroku
DATABASE_URL = os.getenv("postgres://u74paoavmds30r:pf5baba4878a23ad2fa9729b32256b75aa27c1aa49e4fad94e6243afd15ddfae1@c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d196r0fv8p6tii")
connection = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = connection.cursor()

# Function to start the bot
def start(update: Update, context):
    chat_id = update.message.chat_id
    update.message.reply_text('Welcome to SportsFinder bot!')

# Function to register a user (store info in the database)
def register(update: Update, context):
    chat_id = update.message.chat_id
    user_name = ' '.join(context.args)  # Get the user's name from the command

    if user_name:
        # Insert user data into PostgreSQL database
        cursor.execute("INSERT INTO users (chat_id, name) VALUES (%s, %s) ON CONFLICT (chat_id) DO NOTHING", (chat_id, user_name))
        connection.commit()

        update.message.reply_text(f"User {user_name} registered successfully!")
    else:
        update.message.reply_text("Please provide your name after the command. Example: /register John Doe")

# Register the /start and /register commands
start_handler = CommandHandler('start', start)
register_handler = CommandHandler('register', register)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(register_handler)

# Start the bot
updater.start_polling()
updater.idle()

# Close the database connection gracefully when the bot is stopped
connection.close()