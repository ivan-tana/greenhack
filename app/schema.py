from schema import Schema, And, Optional, Use
from datetime import datetime
from .models import USER_TYPES


user_data_schema = Schema({
    'fname': And(str, len),
    'lname': And(str, len),
    'address': And(str, len),
    'active': bool,
    'email': And(str, len),
    'user_type': USER_TYPES,
    Optional('profile_image'): str,
    'tel': And(str, len),
    'birthday': datetime,
    "password": And(str, len),
    Optional('organization'): And(str, len),
    "city": And(str, len),
    "country": And(str, len),


})


org_data_schema = Schema({
    'name': And(str, len),
    'desc': And(str, len),
    'type': And(str, len),
    'user_id': And(int, len)
})