from peewee import *

db = SqliteDatabase('database.sqlite3')


class User(Model):
    identifier = IntegerField()
    first_name = CharField()
    last_name = CharField(null=True)
    username = CharField(null=True)

    class Meta:
        database = db


def get_user(id):
    return User.get_or_none(User.identifier == id)


def create_user(id, first_name, last_name=None, username=None, **params):
    User.create(identifier=id, first_name=first_name, last_name=last_name, username=username)


def update_user(**params):
    User.update(**params).where(User.identifier == params['identifier']).execute()


class Location(Model):
    latitude = FloatField()
    longitude = FloatField()
    display_name = CharField()
    user = ForeignKeyField(User, backref='locations')

    class Meta:
        database = db

def get_location(id):
    return Location.get_or_none(Location.id == id)


def create_location(latitude, longitude, display_name, user):
    Location.create(latitude=latitude, longitude=longitude, display_name=display_name, user=user)


db.connect()
db.create_tables([User], safe=True)
