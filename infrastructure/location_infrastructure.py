from database.db import Location


def get_location(id):
    return Location.get_or_none(Location.id == id)


def create_location(latitude, longitude, display_name, user, timezone):
    Location.create(latitude=latitude, longitude=longitude, display_name=display_name, user=user, timezone=timezone)


def get_all_locations_by_user(user):
    return Location.select().where(Location.user == user)


def delete_location(id):
    location = Location.get_or_none(id)
    if location:
        location.delete_instance()
