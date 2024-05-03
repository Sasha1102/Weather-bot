from peewee import *

db = SqliteDatabase('database.sqlite3')


class User(Model):
    identifier = IntegerField()
    first_name = CharField()
    last_name = CharField(null=True)
    username = CharField(null=True)
    city = CharField(null=True)

    class Meta:
        database = db


def get_user(id):
    return User.get_or_none(User.identifier == id)


def create_user(id, first_name, last_name=None, username=None, **params):
    User.create(identifier=id, first_name=first_name, last_name=last_name, username=username)


def update_user(**params):
    User.update(**params).where(User.identifier == params['identifier']).execute()


db.connect()
db.create_tables([User], safe=True)
