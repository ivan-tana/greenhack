from .models import User
from flask_sqlalchemy import SQLAlchemy
from .schema import user_data_schema
from .models import USER_TYPES
from datetime import datetime
from werkzeug.security import generate_password_hash



def create_user(user_info: dict, db: SQLAlchemy):

    user_data_schema.validate(user_info)

    user = User(
        fname= user_info['fname'],
        lname = user_info['lname'],
        email = user_info['email'],
        user_type =USER_TYPES(user_info['user_type']),
        birthday = datetime.strptime(user_info['birthday'], '%Y-%m-%d'),
        address = user_info['address'],
        tel = user_info['tel'],
        profile_image = user_info['profile_image'],
        active = bool(user_info['active']),
        password = generate_password_hash(user_info['password'])
    )

    db.session.add(user)
    db.session.commit()


def get_users():
    users = []

    all_users = User.query.all()
    for user in all_users:
        
        users.append(user.dict)

    return users




