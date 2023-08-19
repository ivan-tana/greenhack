from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import current_user


from app import database_manipulations as dbM
from app.extensions import db
from app.schema import user_data_schema
from app.models import USER_TYPES, User as UserM
from app  import is_valid


class SingleUser(Resource):
    def get(self, user_id):
        user = UserM.query.filter_by(id=user_id).first()
        if user:
            return user.dict
        return {
            "message": "user dose not exist"
        }, 400

class User(Resource):
    @jwt_required()
    def get(self): 
        return dbM.get_users()
        
    

    
    def post(self):
        user_data_parser = reqparse.RequestParser()

        user_data_parser.add_argument('fname', required=True, help='fname is required' )
        user_data_parser.add_argument('lname', required=True, help='lname is required' )
        user_data_parser.add_argument('address', required=True, help='address is required' )
        user_data_parser.add_argument('email', required=True, help='email is required')
        user_data_parser.add_argument('active' )
        user_data_parser.add_argument('tel', required=True, help='tel is required')
        user_data_parser.add_argument('birthday', required=True, help='birthday is required')
        user_data_parser.add_argument('user_type',  required=True, help='user_type is required' )
        user_data_parser.add_argument('profile_image' )
        user_data_parser.add_argument('password', required=True, help="password is required" )

        args = user_data_parser.parse_args()
    


        if user_data_schema.is_valid(args):
            print(USER_TYPES("personal"))

            if not USER_TYPES(args['user_type']):
                return {"message": f"{is_valid.userType(args['user_type'])} user_type can only have one of the following (PERSONAL,SUPPLIER, BUSINESS ) " }
            
            if is_valid.email_exist(args['email']):
                return {
                    'message': 'an account with this email already exist'
                }, 400
            
            if is_valid.tel_exist(args['tel']):
                return {
                    'message': 'an account with this tel already exist'
                }
            
            dbM.create_user(args, db)

            return {
                "message": "created"
            }, 200
        
        return {
            "message": "invalid data or incomplite data  data must contain [fname, lname, addre, email, tel,birthday, user-type, profile_image, password]" 
        }, 400
    




class Login(Resource):
    def post(self):
        login_parser = reqparse.RequestParser()
        login_parser.add_argument('email', required=True, help="email required")
        login_parser.add_argument('password', required=True, help="password required")

        args = login_parser.parse_args()

        user = UserM.query.filter_by(email = args['email']).first()
        if user:
           if  user.check_password(args['password']):
               return {
                   'token': create_access_token(identity=args['email'])
               }

        return{
            "message": 'invalid login details',
        }, 401

    


class Product(Resource):
    def get(self):
        return {
            "message": "under dev"
        }
    
    def post(self):
        return {
            "message": "under dev"
        }

    def put(self):
        return {
            "message": "under dev"
        }

    def delete(self):
        return {
            "message": "under dev"
        }

