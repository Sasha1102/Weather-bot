from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import services.location_service as ls
import services.user_service as us
import services.ui_service as uis


def register(bot: TeleBot):

    @bot.message_handler(commands=['start'])
    def start_message(m):
        us.create_user_if_not_exist(m.from_user)
        menu_text = uis.main_menu(m.from_user.id)
        bot.send_message(chat_id=m.chat.id, **menu_text)
