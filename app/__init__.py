from flask import Flask, render_template
from pathlib import Path

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager






from .api import api as api_blueprint

from .extensions import db
from . import models


def create_app(config_file='config.py'):
    app = Flask(__name__, template_folder='templates')


    # config app
    app.config.from_pyfile(Path(Path(__file__).parent, config_file))
    
    # register blueprint
    app.register_blueprint(api_blueprint)


    @app.route('/')
    def home():
        return render_template('index.html')




    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id
    
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return models.User.query.filter_by(id=identity).first()



    # init database

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
