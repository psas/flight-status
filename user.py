import bcrypt
import secrets

def auth(username, password):
    if username in secrets.users:
        h = secrets.users[username]
        if bcrypt.hashpw(password, h) == h:
            return True
    return False
