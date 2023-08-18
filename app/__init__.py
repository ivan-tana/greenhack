from flask import Flask
from pathlib import Path


def create_app(config_file='config.py'):
    app = Flask("Green Hack")


    # config app
    app.config.from_pyfile(Path(Path(__file__).parent, config_file))
    
    # register extensions


    print(app.config['SECRET_KEY'])

    return app
