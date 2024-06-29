import telebot
from config import TOKEN
from handlers.message_handlers import register as message_register
from handlers.callback_query_handlers import register as callback_register
from services.schedule_service import start_all_schedules

bot = telebot.TeleBot(TOKEN)

message_register(bot)
callback_register(bot)
start_all_schedules(bot)


if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except Exception as e:
            print(e)
