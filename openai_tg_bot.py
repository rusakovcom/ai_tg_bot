import os
import telebot
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the Telegram bot
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Set up the OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        # Generate a response using OpenAI
        response = client.completions.create(
           model="gpt-3.5-turbo-0125",
            prompt=message.text,
            max_tokens=20
        )
        
        # Send the generated response back to the user
        bot.reply_to(message, response.choices[0].text.strip())
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

# Start the bot
bot.polling()
