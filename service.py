from db import *


def create_user_if_not_exist(user):
    if not get_user(user.id):
        create_user(**user.__dict__)
