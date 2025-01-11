from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

TOKEN = "7537818430:AAFOt1K8xnYUOedx5gaFgvPAkFKUwA9FIdk"

# Assuming you've saved user data in a dictionary or database
user_profiles = {}  # A dictionary to store user profiles

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
        "Hi! You can click on the button below to open up our web app - it’ll give you access to view and edit your profile from there!",
        reply_markup=reply_markup
    )

# /editprofile command or new /profile
async def edit_profile(update: Update, context):
    # Create an InlineKeyboardButton that opens the web app
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
        "Click the button below to view and edit your profile through the web app!",
        reply_markup=reply_markup
    )

# /viewprofile command
'''
async def view_profile(update: Update, context):
    # Create an InlineKeyboardButton that opens the web app
    keyboard = [
        [
            InlineKeyboardButton(
                "View Profile",
                web_app={'url': 'https://barbaracwx.github.io/sportsfinder/?viewprofile=true'}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Click the button below to view your profile through the web app!",
        reply_markup=reply_markup
    )
'''    

# /editmatchpreferences command
async def edit_match_preferences(update: Update, context):
    # Create an InlineKeyboardButton that opens the web app
    keyboard = [
        [
            InlineKeyboardButton(
                "Match Preferences",
                web_app={'url': 'https://barbaracwx.github.io/sportsfinder/edit-match-preferences.html'}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Click the button below to view and edit your match preferences through the web app!",
        reply_markup=reply_markup
    )

'''
# /viewmatchpreferences command
async def view_match_preferences(update: Update, context):
    # Create an InlineKeyboardButton that opens the web app
    keyboard = [
        [
            InlineKeyboardButton(
                "View Match Preferences",
                web_app={'url': 'https://barbaracwx.github.io/sportsfinder/view-match-preferences.html'}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Click the button below to view your match preferences through the web app!",
        reply_markup=reply_markup
    )
    '''



app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("editprofile", edit_profile))
#app.add_handler(CommandHandler("viewprofile", view_profile))
app.add_handler(CommandHandler("editmatchpreferences", edit_match_preferences))
#app.add_handler(CommandHandler("viewmatchpreferences", view_match_preferences))

app.run_polling()
