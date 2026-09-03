users = []

def create_user(name, email):
    user = {
        "name": name,
        "email": email
    }

    users.append(user)
    return user

def get_users():
    return users