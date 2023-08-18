from flask_restful import Resource, reqparse



class User(Resource):
    def get(self):
        return {'message': 'getting user data'}
    


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

