from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import services.location_service as ls
import services.user_service as us


def register(bot: TeleBot):
    def handle_location(m: Message):
        if m.content_type == 'location':
            user = us.get_user(m.from_user.id)
            ls.add_location(m.location.latitude, m.location.longitude, user)
            bot.send_message(m.chat.id, 'Ви додали локацію!')
        else:
            message = bot.send_message(m.chat.id, "Ви надіслали не локацію")
            bot.register_next_step_handler(message, handle_location)

    @bot.callback_query_handler(func=lambda call: call.data == 'menu')
    def menu(call):
        text = "Вітаємо! Оберіть потрібну вам опцію:"
        button_profile = InlineKeyboardButton(text='Список локацій', callback_data='locations_list')
        button_weather_by_coordinates = InlineKeyboardButton(text='Погода за координатами', callback_data='weather_by_coordinates')
        button_distribution = InlineKeyboardButton(text='Розсилка', callback_data='distribution')
        keyboard = InlineKeyboardMarkup()
        keyboard.keyboard = [[button_profile, button_weather_by_coordinates], [button_distribution]]
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data == 'weather_by_coordinates')
    def weather_by_coordinates(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'distribution')
    def distribution(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'time')
    def choose_time(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'duration')
    def duration(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'locations_list')
    def locations(call):
        keyboard = InlineKeyboardMarkup()
        user = us.get_user(call.from_user.id)
        all_locations = ls.get_all_locations_by_user(user)
        text = "Ваші локації" if all_locations else "Ви не додали локації"
        if all_locations:
            for loc in all_locations:
                keyboard.add(InlineKeyboardButton(text=loc.display_name, callback_data=f'location-{loc.id}'))
        keyboard.add(InlineKeyboardButton(text='Додати локацію', callback_data='add_location'))
        keyboard.add(InlineKeyboardButton(text='Меню', callback_data='menu'))
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'location')
    def location(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'add_location')
    def add_location(call):
        bot.edit_message_text('Надішліть вашу локацію', call.message.chat.id, call.message.id)
        bot.register_next_step_handler(call.message, handle_location)

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'remove_location')
    def remove_location(call):
        pass
