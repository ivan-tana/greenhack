from .models import User
from flask_sqlalchemy import SQLAlchemy
from .schema import user_data_schema
from .models import USER_TYPES, Product_category
from datetime import datetime
from werkzeug.security import generate_password_hash



def create_user(user_info: dict, db: SQLAlchemy):

    user_data_schema.validate(user_info)

    user = User(
        **user_info
    )

    db.session.add(user)
    db.session.commit()


def get_users():
    users = []

    all_users = User.query.all()
    for user in all_users:
        
        users.append(user.dict)

    return users




def add_category(category_data: dict, db: SQLAlchemy):
    new_category =  Product_category(
        **category_data
    )

    

