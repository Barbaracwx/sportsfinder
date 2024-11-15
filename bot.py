from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

TOKEN = "7537818430:AAFOt1K8xnYUOedx5gaFgvPAkFKUwA9FIdk"

# Assuming you've saved user data in a dictionary or database
user_profiles = {}  # A dictionary to store user profiles

async def view_profile(update: Update, context):
    user_id = update.message.from_user.id
    # Get the user profile from user_profiles dictionary or database
    user_profile = user_profiles.get(user_id)

    if user_profile:
        # Display the user's profile info directly
        profile_text = f"Age: {user_profile['age']}\n"
        profile_text += f"Gender: {user_profile['gender']}\n"
        profile_text += f"Sports: {user_profile['sports']} | Skill Levels: {user_profile['skill_levels']}\n"
        profile_text += f"Location: {user_profile['location']}"
        await update.message.reply_text(profile_text)
    else:
        await update.message.reply_text("You haven't completed your profile yet. Please use /editprofile to fill it out.")

# /viewprofile command
async def view_profile(update: Update, context):
    # Create an InlineKeyboardButton that opens the web app
    keyboard = [
        [
            InlineKeyboardButton(
                "View Profile",
                web_app={'url': 'https://github.com/Barbaracwx.github.io/sportsfinder?viewprofile=true'}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Click the button below to view your profile through the web app!",
        reply_markup=reply_markup
    )

# /start command
async def start(update: Update, context):
    # Create an InlineKeyboardButton that opens the web app
    keyboard = [
        [
            InlineKeyboardButton(
                "Edit my Profile",
                web_app={'url': 'https://barbaracwx.github.io/sportsfinder/'}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hi! You can click on the button below to open up our web app - it’ll give you access to edit your profile from there!",
        reply_markup=reply_markup
    )

# /editprofile command
async def edit_profile(update: Update, context):
    # Create an InlineKeyboardButton that opens the web app
    keyboard = [
        [
            InlineKeyboardButton(
                "Edit Profile",
                web_app={'url': 'https://barbaracwx.github.io/sportsfinder/'}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Click the button below to edit your profile through the web app!",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("editprofile", edit_profile))
app.add_handler(CommandHandler("viewprofile", view_profile))

app.run_polling()
