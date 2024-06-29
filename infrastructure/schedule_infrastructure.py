from database.db import Schedule


def create_schedule(user, location, hours, minutes):
    return Schedule.create(user=user, location=location, hours=hours, minutes=minutes)


def get_schedule(id):
    return Schedule.get_or_none(Schedule.id == id)


def get_schedules_by_user(user):
    return Schedule.select().where(Schedule.user == user)
