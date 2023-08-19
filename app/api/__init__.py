from flask import Blueprint
from flask_restful import Api




from .resources import \
    User, Product, Login, SingleUser, WhoAmI

api = Blueprint('api', __name__)


rest_api = Api(api)




@api.route('/')
def index():
    return {"message": "Green hack team EUREKA API"}

# register api resources 

rest_api.add_resource(SingleUser, '/user/<user_id>')
rest_api.add_resource(User, '/user')
rest_api.add_resource(Product, '/product')
rest_api.add_resource(Login, '/login')
rest_api.add_resource(WhoAmI, '/whoami')






