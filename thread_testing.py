import threading
from datetime import datetime

now = datetime.now()


def func():
    print('dfgnm')


def time_to_sec(current_hour, current_minute, send_hour, send_minute):
    seconds = 0
    if send_minute >= current_minute:
        seconds += 60*(send_minute-current_minute)
    else:
        seconds += 60*(60+send_minute-current_minute)
        send_hour -= 1
    if send_hour >= current_hour:
        seconds += 3600*(send_hour-current_hour)
    else:
        seconds += 3600*(24+send_hour-current_hour)
    return seconds


print('qwerty')

hour_send = 19
minute_send = 13

timer_seconds = time_to_sec(now.hour, now.minute, hour_send, minute_send)
threading.Timer(timer_seconds, func).start()
