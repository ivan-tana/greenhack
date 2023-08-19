from .extensions import db
from werkzeug.security import check_password_hash
from datetime import datetime

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
    country = db.Column(db.String(60))
    city = db.Column(db.String(60))
    tel = db.Column(db.String(30))
    email = db.Column(db.String(60))
    active = db.Column(db.Boolean, default=True)
    profile_image = db.Column(db.Text)
    password = db.Column(db.Text)
    products = db.relationship('Product', backref='user')
    # organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))


    @property
    def dict(self):
        return {
            'id': self.id,
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
    def check_password(self, password):
        return check_password_hash(self.password, password)





        
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    desc = db.Column(db.Text)
    create_at = db.Column(db.Date, default=datetime.utcnow())
    modified_at = db.Column(db.Date, default=datetime.utcnow())
    images = db.relationship('Product_images', backref='product')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float)
    address = db.Column(db.String(60))

    @property
    def dict(self):
        return {
            "name": self.name,
            "images": [image.dict for image in self.images],
            "user_id": self.user_id,
            "desc": self.desc,
            "id": self.id
        }  

    
# temp

class Product_purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer)
    product_id  =  db.Column(db.Integer)
    complete = db.Column(db.Boolean)




class Product_images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    caption = db.Column(db.String(60))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    

    @property
    def dict(self):
        return {
            "product_id": self.product_id,
            "url": self.url,
            "id": self.id
        }



