from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def register(bot):
    @bot.callback_query_handler(func=lambda call: call.data == 'menu')
    def menu(call):
        text = "Вітаємо! Оберіть потрібну вам опцію:"
        button_profile = InlineKeyboardButton(text='Профіль', callback_data='profile')
        button_weather_by_coordinates = InlineKeyboardButton(text='Погода за координатами', callback_data='weather_by_coordinates')
        button_distribution = InlineKeyboardButton(text='Розсилка', callback_data='distribution')
        keyboard = InlineKeyboardMarkup()
        keyboard.keyboard = [[button_profile, button_weather_by_coordinates], [button_distribution]]
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: call.data == 'profile')
    def profile(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'weather_by_coordinates')
    def weather_by_coordinates(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'distribution')
    def distribution(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'change_city')
    def change_city(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'time')
    def choose_time(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'duration')
    def duration(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'locations')
    def locations(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'location')
    def location(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'remove_location')
    def remove_location(call):
        pass
