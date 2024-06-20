from peewee import IntegerField
from database.db import User


def migrate(migrator, database, fake=False, **kwargs):
    with database.atomic():
        migrator.add_fields(
            User,
            favourite_location=IntegerField(null=True)
        )


def rollback(migrator, database, fake=False, **kwargs):
    with database.atomic():
        migrator.remove_fields(User, 'favourite_location')
