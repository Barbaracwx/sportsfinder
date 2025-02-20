import os
import psycopg2
import json
import aiohttp  # Use aiohttp for async requests
import asyncio
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Application, CallbackContext
from telegram.ext import MessageHandler, filters
import logging

logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Create the Application object
application = Application.builder().token(TOKEN).build()

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
connection = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = connection.cursor()

# Confirm the database connection
cursor.execute("SELECT current_database();")
current_database = cursor.fetchone()
print(f"Connected to database: {current_database[0]}")

# Function to start the bot
async def start(update: Update, context: CallbackContext):
    user_telegram_id = update.message.from_user.id
    user_first_name = update.message.from_user.first_name

    try:
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
    keyboard = [[
        InlineKeyboardButton("My Profile", web_app={'url': 'https://barbaracwx.github.io/sportsfinder/'})
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Hello {user_first_name}, welcome to Sportsfinder!\n\n"
        "Are you ready to find your sports partner?\n\n"
        "Click the button below to set up your profile.",
        reply_markup=reply_markup
    )

async def set_webhook():
    webhook_url = 'https://a6ec-137-132-26-143.ngrok-free.app/webhook'  # Your actual webhook URL

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook', params={'url': webhook_url}) as response:
            data = await response.json()
            if data.get("ok"):
                logging.info("Webhook set successfully!")
            else:
                logging.error(f"Failed to set webhook: {data}")

# Register the /start command
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

# Main function to start the bot
async def main():
    await set_webhook()  # Ensure the webhook is properly set
    logging.info("Bot is now waiting for incoming webhooks...")
    await application.run_webhook(listen="0.0.0.0", port=8080, url_path=TOKEN)

if __name__ == "__main__":
    asyncio.run(main())  # Run the async bot properly
