import telebot
from config import TOKEN
from service import *

bot = telebot.TeleBot(TOKEN)


def handle_city(m):
    change_city(m)


@bot.message_handler(commands=['start'])
def start_message(m):
    if create_user_if_not_exist(m.from_user):
        msg = bot.send_message(m.chat.id, "Вітаємо! Напишіть ваше місто")
        bot.register_next_step_handler(msg, handle_city)
    if not get_city(m.from_user.id):
        msg = bot.send_message(m.chat.id, "Вітаємо! Напишіть ваше місто")
        bot.register_next_step_handler(msg, handle_city)


if __name__ == '__main__':
    bot.polling()
