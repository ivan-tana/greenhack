from .models import User
from flask_sqlalchemy import SQLAlchemy
from .schema import user_data_schema
from .models import USER_TYPES, Product, Product_images
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_jwt_extended import current_user


def create_user(user_info: dict, db: SQLAlchemy):

    user_data_schema.validate(user_info)

    user = User(
        **user_info
    )
    try:

        db.session.add(user)
        db.session.commit()
    except:
        return None
    return user


def get_users():
    users = []

    all_users = User.query.all()
    for user in all_users:
        
        users.append(user.dict)

    return users


def add_product(data: dict, db: SQLAlchemy):
    new_product = Product(
        **data
    )

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        return None
    return new_product

def get_product():
    products = []
    for product in Product.query.all():
        products.append(product.dict)
    return products


def add_product_image(data: dict, db: SQLAlchemy):
    new_image = Product_images(
        **data
    )
    try: 
        db.session.add(new_image)
        db.session.commit()
    except:
        return None 
    return new_image


def get_images(product_id):
    images = []
    product = Product.query.get(product_id)
    for  image in product.images:
        images.append(image.dict)
    return images


    


# def checkout_product(product_id, db:SQLAlchemy):
#     new_check = Check_out(
#         user_id = current_user.id,
#         product_id = product_id
#     )
#     try: 
#         db.session.add(new_check)
#         db.session.commit()
#     except:
#         return None 
#     return new_check

