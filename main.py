import telebot
from config import TOKEN
from service import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(m):
    create_user_if_not_exist(m.from_user)
    bot.send_message(m.chat.id, "о")


if __name__ == '__main__':
    bot.polling()
