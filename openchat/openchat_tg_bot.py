# Openchat model by https://serverspace.ru/services/serverspace-gpt-api/
# This openchat_tg_bot.py run telegram bot, requests to model and getting answer - through another script in this dit request_to_chat.py 

import os
import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define your bot token
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN') 

# Function to handle the start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send any text, and it will respond with the output of request_to_chat.py.')

# Function to handle received messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    
    # Run the request_to_chat.py script with the user input
    result = subprocess.run(['python3', 'request_to_chat.py', user_input], capture_output=True, text=True)
    
    # Get the output from the script
    response = result.stdout.strip()
    
    # Send the response back to the user
    update.message.reply_text(response)

def main() -> None:
    # Create the Updater and pass it bot's token
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register a message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()

