import os
import psycopg2
import json
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Application, CallbackContext
from telegram.ext import MessageHandler, filters
import requests
import logging

logging.basicConfig(level=logging.DEBUG)


# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Create the Application object
application = Application.builder().token(TOKEN).build()

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
connection = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = connection.cursor()

# Print the current database to confirm the connection
cursor.execute("SELECT current_database();")
current_database = cursor.fetchone()
print(f"Connected to database: {current_database[0]}")

# Function to start the bot
async def start(update: Update, context: CallbackContext):
    user_telegram_id = update.message.from_user.id
    user_first_name = update.message.from_user.first_name

    try:
        # Insert user into database (only chat_id)
        cursor.execute(
            "INSERT INTO users (chat_id, name) VALUES (%s, %s) ON CONFLICT (chat_id) DO NOTHING",
            (user_telegram_id, user_first_name)
        )
        connection.commit()
        print(f"User {user_telegram_id} registered in database.")

    except Exception as e:
        connection.rollback()
        print(f"Database error: {e}")

    # Create a button to access the web app
    keyboard = [
        [
            InlineKeyboardButton(
                "My Profile",
                web_app={'url': 'https://barbaracwx.github.io/sportsfinder/'}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send welcome message
    await update.message.reply_text(
        f"Hello {user_first_name}, welcome to Sportsfinder!\n\n"
        "Are you ready to find your sports partner?\n\n"
        "Click the button below to set up your profile.",
        reply_markup=reply_markup
    )

def handle_profile_data(data):
    """Function to handle the data received from the web app."""
    try:
        # Extract data from the request
        chat_id = data.get('chat_id')
        age = data.get('age')
        gender = data.get('gender')
        sports = data.get('sports')
        location = data.get('location')

        # You can now process this data (e.g., updating the user profile in the bot)
        logging.info(f"Processing profile data for chat_id: {chat_id}")

        # Example: Send the profile information back to the user via the Telegram bot
        send_profile_data_to_user(chat_id, age, gender, sports, location)

    except Exception as e:
        logging.error(f"Error processing profile data: {e}")

async def send_profile_data_to_user(chat_id, age, gender, sports, location):
    """Send profile data back to the user using the Telegram bot."""
    try:
        message = f"Profile Information:\nAge: {age}\nGender: {gender}\nSports: {sports}\nLocation: {location}"
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            logging.info(f"Successfully sent message to chat_id: {chat_id}")
        else:
            logging.error(f"Failed to send message to chat_id: {chat_id}")
    
    except Exception as e:
        logging.error(f"Error sending profile data: {e}")  

# Function to set the webhook (to be called once)
async def set_webhook():

    webhook_url = 'https://sportsfinder-production-app.herokuapp.com/webhook'  # Update with your actual URL
    response = requests.post(f'https://api.telegram.org/bot{TOKEN}/setWebhook', data={'url': webhook_url})

    if response.status_code == 200:
        logging.info("Webhook set successfully!")
    else:
        logging.error(f"Failed to set webhook: {response.status_code}")


# Register the /start command
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Set webhook on initialization (make sure to await this)
async def main():
    await set_webhook()  # Ensure set_webhook is awaited
    logging.info("Bot is now waiting for incoming webhooks...")
    application.application.run_webhook()


