import os
from datetime import timedelta
SECRET_KEY = os.getenv('secret_key')
JWT_SECRET_KEY = os.getenv('jwt_secret_key')
SQLALCHEMY_DATABASE_URI = os.getenv('database_uri')
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
