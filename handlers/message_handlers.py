from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import services.location_service as ls
import services.user_service as us


def register(bot: TeleBot):

    @bot.message_handler(commands=['start'])
    def start_message(m):
        us.create_user_if_not_exist(m.from_user)
        text = "Вітаємо! Оберіть потрібну вам опцію:"
        button_profile = InlineKeyboardButton(text='Список локацій', callback_data='locations_list')
        button_weather_by_coordinates = InlineKeyboardButton(
            text='Погода за координатами',
            callback_data='weather_by_coordinates'
        )
        button_distribution = InlineKeyboardButton(text='Розсилка', callback_data='distribution')
        keyboard = InlineKeyboardMarkup()
        keyboard.keyboard = [[button_profile, button_weather_by_coordinates], [button_distribution]]
        bot.send_message(chat_id=m.chat.id, text=text, reply_markup=keyboard)
