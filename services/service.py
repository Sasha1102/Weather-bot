from db import *


def create_user_if_not_exist(user):
    if not get_user(user.id):
        create_user(**user.__dict__)
        return True
    return False


def change_city(m):
    update_user(identifier=m.from_user.id, city=m.text)


def get_city(user_id):
    user = get_user(user_id)
    return user.city


def main_menu():
    pass

