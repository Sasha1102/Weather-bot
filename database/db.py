from peewee import *

db = SqliteDatabase('database.sqlite3')


class User(Model):
    identifier = IntegerField()
    first_name = CharField()
    last_name = CharField(null=True)
    username = CharField(null=True)
    favourite_location = IntegerField(null=True)

    class Meta:
        database = db


class Location(Model):
    latitude = FloatField()
    longitude = FloatField()
    display_name = CharField()
    user = ForeignKeyField(User, backref='locations')

    class Meta:
        database = db


db.connect()
db.create_tables([User, Location], safe=True)
