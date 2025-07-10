import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os

# استخدم التوكن من متغير بيئة
API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_roastyface(message):
    markup = InlineKeyboardMarkup()
    mini_app_url = "https://roastyface.vercel.app"  # ضع هنا رابط Vercel بعد النشر
    btn = InlineKeyboardButton("🔥 Roast Me Now", web_app=WebAppInfo(url=mini_app_url))
    markup.add(btn)
    bot.send_message(
        message.chat.id,
        "Welcome to RoastyFace 😈\nLet the AI roast you... if you dare!",
        reply_markup=markup
    )

bot.polling()
