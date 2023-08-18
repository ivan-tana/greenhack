from flask import Blueprint
from flask_restful import Api


from .resources import \
    User

api = Blueprint('api', __name__)


rest_api = Api(api)


@api.route('/')
def index():
    return {"message": "Green hack team EUREKA API"}

# register api resources 

rest_api.add_resource(User, '/user')





