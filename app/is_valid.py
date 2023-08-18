
from .models import USER_TYPES, User

def  userType(value):
    try:
        USER_TYPES(value)
        return True
    finally:
        return False



def email_exist(email):
    if User.query.filter_by(email=email).first():
        return True
    return False

def tel_exist(value):
    if User.query.filter_by(tel=value).first():
        return True
    return False
