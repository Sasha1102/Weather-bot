from database.db import Location


def get_location(id):
    return Location.get_or_none(Location.id == id)


def create_location(latitude, longitude, display_name, user):
    Location.create(latitude=latitude, longitude=longitude, display_name=display_name, user=user)


def get_all_locations_by_user(user):
    return Location.select().where(Location.user == user)
