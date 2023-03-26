from flask import abort, jsonify
from flask_restful import Resource, request, reqparse
from Models import UserModel
from sqlalchemy.exc import SQLAlchemyError 



class User(Resource):
     def get(self, id):
         user = UserModel.find_by_id(id)
         if user:
             return jsonify(user.serialize())
         return {'message': 'user not found'}, 404

     def delete(self, id):
         store = UserModel.find_by_id(id)
         if store:
            store.delete_from_db()
         return {"message": "user deleted successfully."}, 201


class UserRegister(Resource):
     def post(self):
        data = request.get_json()
        # if UserModel.find_by_id(data['username']):
        #     return {"message": "A user with that username already exists"}, 400
      #   print(**data)
        try:
         user = UserModel(**data)
         print(user)
        #user = UserModel(data['username'], data['password']) # unpacking user = UserModel(**data)
         user.save_to_db()
         return jsonify(user.serialize())
         
        except SQLAlchemyError as e:
         return {'message': "A user with name '{}' already exists.". format(user.username)}, 400



        
