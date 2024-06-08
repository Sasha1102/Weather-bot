import requests
import pytz
from datetime import datetime


# url = 'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_probability_max,wind_speed_10m_max,wind_gusts_10m_max&forecast_days=1&timezone=auto'
url = 'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,rain,showers,snowfall,wind_speed_10m,wind_gusts_10m&forecast_days=1'

gmt_timezone = pytz.timezone('Etc/GMT')


def get_weather(location):
    response = requests.get(url.format(latitude=location.latitude, longitude=location.longitude))
    current_datetime = datetime.now(gmt_timezone)
    current_hour = current_datetime.hour
    data = response.json()
    current_weather = {
        'temperature': data['hourly']['temperature_2m'][current_hour],
        'humidity': data['hourly']['relative_humidity_2m'][current_hour],
        'rain': data['hourly']['rain'][current_hour],
        'showers': data['hourly']['showers'][current_hour],
        'snowfall': data['hourly']['snowfall'][current_hour],
        'wind_speed': data['hourly']['wind_speed_10m'][current_hour],
        'wind_gusts': data['hourly']['wind_gusts_10m'][current_hour]
    }
    return current_weather
