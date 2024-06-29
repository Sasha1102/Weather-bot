from database.db import User


def get_user(user_id):
    return User.get_or_none(User.identifier == user_id)


def create_user(id, first_name, last_name=None, username=None, **params):
    User.create(identifier=id, first_name=first_name, last_name=last_name, username=username)


def update_user(**params):
    User.update(**params).where(User.identifier == params['identifier']).execute()


def get_all_users():
    return User.select()
