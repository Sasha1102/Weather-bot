from db import *
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='geoapiExercises')


def create_user_if_not_exist(user):
    if not get_user(user.id):
        create_user(**user.__dict__)
        return True
    return False


def add_location(identifier, latitude, longitude):
    location = geolocator.reverse((latitude, longitude), language='en')
    user = get_user(identifier)
    create_location(latitude, longitude, location.adress, user)


def get_city(user_id):
    user = get_user(user_id)
    return user.city


def main_menu():
    pass
