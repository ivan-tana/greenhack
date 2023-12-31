from flask import Blueprint, render_template
from flask_restful import Api




from .resources import \
    User, Product, Login, SingleUser, WhoAmI, Product_image

api = Blueprint('api', __name__, url_prefix='/api')


rest_api = Api(api)







# register api resources 

rest_api.add_resource(SingleUser, '/user/<user_id>')
rest_api.add_resource(User, '/user')
rest_api.add_resource(Product, '/product')
rest_api.add_resource(Login, '/login')
rest_api.add_resource(WhoAmI, '/whoami')
rest_api.add_resource(Product_image, '/product/<product_id>/image')











