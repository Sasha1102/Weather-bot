import infrastructure.user_infrastructure as ui


def create_user_if_not_exist(user):
    if not ui.get_user(user.id):
        ui.create_user(**user.__dict__)
        return True
    return False


def get_user(user_id):
    return ui.get_user(user_id)
