from .extensions import db

from enum import Enum

class USER_TYPES(Enum):
    PERSONAL = 'personal'
    SUPPLIER = 'supplier'
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
    active = db.Column(db.Boolean, default=True)
    profile_image = db.Column(db.Text)
    password = db.Column(db.Text)

    @property
    def dict(self):
        return {
            'fname': self.fname,
            'lname':self.lname,
            'birthday': str(self.birthday),
            'user_type': self.user_type.value,
            'tel': self.tel,
            'address': self.address,
            'email': self.email,
            'active': self.active,
            'profile_image': self.profile_image,
        }

    
