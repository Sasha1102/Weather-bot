import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from config import TOKEN
from services.service import *

bot = telebot.TeleBot(TOKEN)


def handle_city(m):
    change_city(m)


@bot.message_handler(commands=['start'])
def start_message(m):
    if create_user_if_not_exist(m.from_user):
        msg = bot.send_message(m.chat.id, "Вітаємо! Напишіть ваше місто")
        bot.register_next_step_handler(msg, handle_city)
    elif not get_city(m.from_user.id):
        msg = bot.send_message(m.chat.id, "Вітаємо! Напишіть ваше місто")
        bot.register_next_step_handler(msg, handle_city)
    button2 = KeyboardButton(text="Share Location", request_location=True)
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    # button1 = InlineKeyboardButton(text="CВ", url="https://google.com")
    # keyboard.keyboard = [[button1]]
    # bot.send_message(m.chat.id, "йцукен", reply_markup=keyboard)
    keyboard.add(button2)
    bot.send_message(m.chat.id, "йцукен2", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == '')
def callback_inline(call):
    if call.data == "SS":
        pass

if __name__ == '__main__':
    bot.polling()
