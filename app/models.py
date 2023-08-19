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
    cart = db.relationship("Cart", backref='user')
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


# class Organization(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.relationship('User', backref='organization')
#     name = db.Column(db.String(30))
#     desc = db.Column(db.Text)
#     type = db.Column(db.String(30))

#     @property
#     def dict(self):
#         return {
#             'name': self.name,
#             'desc': self.desc,
#             'type': self.type
#         }


        
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


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    card_items = db.relationship('Cart_item', backref='cart')

    @property
    def dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "cart_items": [item.dict for item in self.card_items]
        }

class Cart_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.Date, default=datetime.utcnow())


    @property
    def dict(self):
        return{
            "id": self.id,
            "product_id": self.product_id,
            "created_at": str(self.created_at)
        }
    




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







# class Order_details(db.Model):
#     id =  db.Column(db.Integer, primary_key=True)
#     total = db.Column(db.Float)
#     create_at = db.Column(db.Date, default=datetime.utcnow())
#     modified_at = db.Column(db.Date, default=datetime.utcnow())
#     user_id = db.relationship('User', backref='order_details') 
#     payment_id = db.relationship('Payment_details', backref='order_details') 

# class Order_item(db.Model):
#     id =  db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.Integer)
#     user_id = db.relationship('User', backref='order_item') 
#     payment_id = db.relationship('Payment_details', backref='order_item') 
#     order_id = db.relationship('Order_details', backref="order_item") 
#     product_id = db.relationship("Product", backref="order_item") 


# class Payment_details(db.Model):
#     id =  db.Column(db.Integer, primary_key=True)
#     order_id = db.relationship('Order_details', backref='payment_details')
#     amount = db.Column(db.Float)
#     status = db.Column(db.String(30))
#     created_at = db.Column(db.Date, default=datetime.utcnow())
#     modifid_at = db.Column(db.Date, default=datetime.utcnow())

# class Cart(db.Model):
#     pass 

# class User_payment():
#     pass





