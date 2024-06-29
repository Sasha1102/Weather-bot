import infrastructure.schedule_infrastructure as si
import services.ui_service as uis
import services.weather_service as ws
import infrastructure.user_infrastructure as ui
import threading
from datetime import datetime


def time_to_sec(current_hour, current_minute, send_hour, send_minute):
    seconds = 0
    send_minute -= 1
    if send_minute >= current_minute:
        seconds += 60*(send_minute-current_minute)
    else:
        seconds += 60*(60+send_minute-current_minute)
        send_hour -= 1
    if send_hour >= current_hour:
        seconds += 3600*(send_hour-current_hour)
    else:
        seconds += 3600*(24+send_hour-current_hour)
    return seconds + 60


def start_distribution(bot, user, schedule):
    weather = ws.get_weather(schedule.location)
    text = uis.create_weather_text(weather, schedule.location)
    bot.send_message(user.identifier, text=text)
    start_single_schedule(bot, schedule, user)


def start_single_schedule(bot, schedule, user):
    now = datetime.now()
    timer_seconds = time_to_sec(now.hour, now.minute, schedule.hours, schedule.minutes)
    threading.Timer(timer_seconds, start_distribution, args=[bot, user, schedule]).start()


def start_all_schedules(bot):
    users = ui.get_all_users()
    for user in users:
        schedules = si.get_schedules_by_user(user)
        for schedule in schedules:
            start_single_schedule(bot, schedule, user)
