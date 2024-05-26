import telebot
from config import TOKEN
from handlers.message_handlers import register as message_register
from handlers.callback_query_handlers import register as callback_register

bot = telebot.TeleBot(TOKEN)

message_register(bot)
callback_register(bot)

if __name__ == '__main__':
    bot.polling()
