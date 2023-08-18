from .models import User
from flask_sqlalchemy import SQLAlchemy
from .schema import user_data_schema





def create_user(user_info: dict, db: SQLAlchemy):
    
    user_data_schema.validate(user_info)

    user = User(
        fname= user_info['fname'],
        lname = user_info['lname'],
        email = user_info['email'],
        user_type = user_info['user_type'],
        birthday = user_info['birthday'],
        address = user_info['address'],
        tel = user_info['tel'],
        profile_image = user_info['profile_image'],
        active = user_info['active'] or True
    )

    db.session.add(user)
    db.session.commit()


def get_users():
    return User.query.all()




