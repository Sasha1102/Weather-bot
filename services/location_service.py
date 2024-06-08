from geopy.geocoders import Photon
import infrastructure.location_infrastructure as li


geolocator = Photon(user_agent='geoapiExercises')


def add_location(latitude, longitude, user):
    location = geolocator.reverse((latitude, longitude), language='en')
    address = []
    if not location:
        address = f'{latitude}, {longitude}'
    elif len(location.address.split(', ')) >= 6:
        for i in range(-1, -7, -1):
            if i not in (-4, -5):
                address.append(location.address.split(', ')[i])
        address = ', '.join(address)
    else:
        address = ', '.join(location.address.split(', ')[::-1])
    li.create_location(latitude, longitude, address, user)


def get_all_locations_by_user(user):
    return li.get_all_locations_by_user(user)


def get_location(id):
    return li.get_location(id)
