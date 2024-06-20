from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import services.location_service as ls
import services.user_service as us
import services.weather_service as ws


def create_weather_text(weather, location_instance):
    wind_speed = round(weather['wind_speed'] / 3.6, 2)
    wind_gusts = round(weather['wind_gusts'] / 3.6, 2)
    text = (f"Поточна погода у {location_instance.display_name}:\n"
            f"Температура: {weather['temperature']}°C\n"
            f"Відносна вологість: {weather['humidity']}%\n"
            f"Дощ: {int(weather['rain'])}%\n"
            f"Злива: {int(weather['showers'])}%\n"
            f"Снігопад: {int(weather['snowfall'])}%\n"
            f"Швидкість вітру: {wind_speed}м/с\n"
            f"Пориви вітру: {wind_gusts}м/с\n")
    return text


def main_menu(user_id):
    user = us.get_user(user_id)
    text = 'Вітаємо!\n'
    if user.favourite_location:
        location_instance = ls.get_location(user.favourite_location)
        weather = ws.get_weather(location_instance)
        weather_text = create_weather_text(weather, location_instance)
        text += f'Ваша улюблена локація: {location_instance.display_name}\n'
        text += weather_text

    text += "Оберіть потрібну вам опцію:"
    button_profile = InlineKeyboardButton(text='Список локацій', callback_data='locations_list')
    button_weather_by_coordinates = InlineKeyboardButton(
        text='Погода за координатами',
        callback_data='weather_by_coordinates'
    )
    button_distribution = InlineKeyboardButton(text='Розсилка', callback_data='distribution')
    keyboard = InlineKeyboardMarkup()
    keyboard.keyboard = [[button_profile, button_weather_by_coordinates], [button_distribution]]
    return {
        'text': text,
        'reply_markup': keyboard
    }