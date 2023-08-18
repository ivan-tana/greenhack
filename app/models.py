from .extensions import db

from enum import Enum

class USER_TYPES(Enum):
    PERSONAL = 'personal'
    SUPPLIER = 'supplier '
    BUSINESS = 'business'



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    birthday = db.Column(db.Date)
    user_type = db.Column(db.Enum(USER_TYPES))
    address = db.Column(db.String(60))
    tel = db.Column(db.String(30))
    email = db.Column(db.String(60))
    active = db.Column(db.Boolean, defualt=True)
    profile_image = db.Column(db.Text)

    
