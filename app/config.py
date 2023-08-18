import os
SECRET_KEY = os.getenv('secret_key')
SQLALCHEMY_DATABASE_URI = os.getenv('database_uri')
SQLALCHEMY_TRACK_MODIFICATIONS = False

