from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from services.service import *


def register(bot):
    def handle_location(m):
        if m.content_type == 'location':
            add_location(m.from_user.id, m.location.latitude, m.location.longitude)
        else:
            m = "Ви надіслали не локацію"
            bot.register_next_step_handler(m, handle_location)

    @bot.message_handler(commands=['start'])
    def start_message(m):
        create_user_if_not_exist(m.from_user)
        text = "Вітаємо! Оберіть потрібну вам опцію:"
        button_profile = InlineKeyboardButton(text='Профіль', callback_data='profile')
        button_weather_by_coordinates = InlineKeyboardButton(text='Погода за координатами', callback_data='weather_by_coordinates')
        button_distribution = InlineKeyboardButton(text='Розсилка', callback_data='distribution')
        keyboard = InlineKeyboardMarkup()
        keyboard.keyboard = [[button_profile, button_weather_by_coordinates], [button_distribution]]
        bot.send_message(chat_id=m.chat.id, text=text, reply_markup=keyboard)
