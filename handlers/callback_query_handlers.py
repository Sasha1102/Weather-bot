from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import services.location_service as ls
import services.user_service as us
import services.weather_service as ws
import services.ui_service as uis
import services.schedule_service as ss
import re
from datetime import datetime
import infrastructure.schedule_infrastructure as si


def register(bot: TeleBot):
    def handle_location(m: Message):
        if m.content_type == 'location':
            user = us.get_user(m.from_user.id)
            ls.add_location(m.location.latitude, m.location.longitude, user)
            bot.send_message(m.chat.id, 'Ви додали локацію!')
            menu_text = uis.main_menu(m.from_user.id)
            bot.send_message(chat_id=m.chat.id, **menu_text)
        else:
            if m.text == 'stop':
                bot.send_message(m.chat.id, "Ви скасували надсилання")
                menu_text = uis.main_menu(m.from_user.id)
                bot.send_message(chat_id=m.chat.id, **menu_text)
                return
            message = bot.send_message(m.chat.id, "Ви надіслали не локацію")
            bot.register_next_step_handler(message, handle_location)

    def handle_schedule_time(m):
        if m.text == 'stop':
            bot.send_message(m.chat.id, "Ви скасували надсилання")
            menu_text = uis.main_menu(m.from_user.id)
            bot.send_message(chat_id=m.chat.id, **menu_text)
            return
        time_str = m.text
        pattern = re.compile(r'^(?:[01]\d|2[0-3]):[0-5]\d$')
        if not pattern.match(time_str):
            bot.send_message(m.chat.id, text='Ви написали час в неправильному форматі')
            bot.register_next_step_handler(m, handle_schedule_time)
            return
        time_obj = datetime.strptime(time_str, "%H:%M")

        hour = time_obj.hour
        minute = time_obj.minute
        user = us.get_user(m.from_user.id)
        schedule = si.create_schedule(user, user.favourite_location, hour, minute)
        ss.start_single_schedule(bot, schedule, user)
        bot.send_message(m.chat.id, 'Ви додали розсилку!')
        menu_text = uis.main_menu(m.from_user.id)
        bot.send_message(chat_id=m.chat.id, **menu_text)

    @bot.callback_query_handler(func=lambda call: call.data == 'menu')
    def menu(call):
        menu_text = uis.main_menu(call.from_user.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, **menu_text)

    @bot.callback_query_handler(func=lambda call: call.data == 'weather_by_coordinates')
    def weather_by_coordinates(call):
        pass

    @bot.callback_query_handler(func=lambda call: call.data == 'distribution')
    def distribution(call):
        keyboard = InlineKeyboardMarkup()
        user = us.get_user(call.from_user.id)
        if not user.favourite_location:
            bot.answer_callback_query(call.id, text='У вас немає улюбленої локації, додайте її', show_alert=True)
            return
        bot.edit_message_text(text='Впишіть час для розсилки', chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyboard)
        bot.register_next_step_handler(call.message, handle_schedule_time)

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
        location_id = int(call.data.split('-')[1])
        location_instance = ls.get_location(location_id)
        user = us.get_user(call.from_user.id)
        weather = ws.get_weather(location_instance)
        text = uis.create_weather_text(weather, location_instance)
        keyboard = InlineKeyboardMarkup()
        if user.favourite_location == location_id:
            keyboard.add(InlineKeyboardButton(text='Прибрати локацію з улюбленої',
                                              callback_data=f'rm_from_fav-{location_id}'))
        else:
            keyboard.add(InlineKeyboardButton(text='Зробити локацію улюбленою',
                                              callback_data=f'set_fav-{location_id}'))
        keyboard.add(InlineKeyboardButton(text='Видалити локацію', callback_data=f'remove_location-{location_id}'))
        keyboard.add(InlineKeyboardButton(text='Список локацій', callback_data='locations_list'))
        bot.edit_message_text(text, call.message.chat.id, call.message.id, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data == 'add_location')
    def add_location(call):
        bot.edit_message_text('Надішліть вашу локацію', call.message.chat.id, call.message.id)
        bot.register_next_step_handler(call.message, handle_location)

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'remove_location')
    def remove_location(call):
        location_id = int(call.data.split('-')[1])
        ls.delete_location(location_id)
        user = us.get_user(call.from_user.id)
        user.favourite_location = None
        user.save()
        bot.answer_callback_query(call.id, text='Ви видалили локацію')
        locations(call)

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'rm_from_fav')
    def rm_from_fav(call):
        user = us.get_user(call.from_user.id)
        user.favourite_location = None
        user.save()
        bot.answer_callback_query(call.id, text='Ви вилучили цю локацію із улюблених')
        location(call)

    @bot.callback_query_handler(func=lambda call: call.data.split('-')[0] == 'set_fav')
    def set_fav(call):
        location_id = int(call.data.split('-')[1])
        user = us.get_user(call.from_user.id)
        user.favourite_location = location_id
        user.save()
        bot.answer_callback_query(call.id, text='Ви зробили цю локацію улюбленою')
        location(call)
