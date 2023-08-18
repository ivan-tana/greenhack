from flask import Flask
from pathlib import Path

from .api import api as api_blueprint

from .extensions import db
from . import models


def create_app(config_file='config.py'):
    app = Flask("Green Hack")


    # config app
    app.config.from_pyfile(Path(Path(__file__).parent, config_file))
    
    # register blueprint
    app.register_blueprint(api_blueprint)


    # init database

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
