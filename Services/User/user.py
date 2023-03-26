from flask import abort, jsonify
from flask_restful import Resource, request, reqparse
from Models import UserModel
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, NoReferencedTableError

from schemas import UserSchema, UserUpdateSchema 

#https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/33781460#overview
blp = Blueprint("users", __name__, description="Operations on users")

@blp.route("/user/<string:id>")
class User(MethodView):
     @blp.response(200, UserSchema)  #UserSchema is used to serialize the data into JSON instead of creating a serialize() method
     def get(self, id):
         user = UserModel.find_by_id(id)
         if user:
            return user
         else:
            return {'message': 'user not found'}, 404

     def delete(self, id):
         store = UserModel.find_by_id(id)
         if store:
            store.delete_from_db()
         return {"message": "user deleted successfully."}, 201

#https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/
     @blp.arguments(UserUpdateSchema)   # validating the fields to update to be passed as payload to this route
     @blp.response(201, UserSchema)
     def put(self, user_data, id):
        try:
            user = UserModel.find_by_id(id)
            print('user =>', user)
            if user:
                user.email = user_data["email"]
                user.password = user_data["password"]
                return user
            else:
                user = UserModel(id=id,**user_data) #user = UserModel(data['username'], data['password']) # unpacking user = UserModel(**data)
                user.save_to_db()

        except NoReferencedTableError:
            abort(422, message= "Please create a region before you add a user" )
        except SQLAlchemyError:
            abort(500, message= "An error occurred while adding the user" )


@blp.route("/user")
class UserRegister(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        users = UserModel.findAll()
        return users

    @blp.arguments(UserSchema)   # validating the fields to be pass as payload to this route
    @blp.response(201, UserSchema)
    def post(self, user_data):
        # user_data = request.get_json(force=True)
        # if UserModel.find_by_id(data['username']):
        #     return {"message": "A user with that username already exists"}, 400
      #   print(**data)
        try:
         user = UserModel(**user_data) #user = UserModel(data['username'], data['password']) # unpacking user = UserModel(**data)
         user.save_to_db()
         return user
                              #https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/33781460#overview
        except NoReferencedTableError:
            abort(422, message= "Please create a region before you add a user" )
        except SQLAlchemyError:
            abort(500, message= "An error occurred while adding the user" )


   
        

       


        
