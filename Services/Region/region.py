from flask import abort, jsonify   # https://flask.palletsprojects.com/en/2.2.x/
from flask_restful import Resource, request, reqparse
from Models import RegionModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError  # error when violating foreignkey/primary integrity  #https://docs.sqlalchemy.org/en/20/core/exceptions.html



class Region(Resource):
     def post(self):
        data = request.get_json()
        # if UserModel.find_by_id(data['username']):
        #     return {"message": "A user with that username already exists"}, 400
      #   print(**data)
        try:
         region = RegionModel(data)  # call regionModel constructor
         print(region)
         region.save_to_db()    # save to the database through the model
         return jsonify(region.serialize())    # turn the region object to json

        except IntegrityError:                  
         return {'message': "A region with name '{}' already exists.". format(region.name_of_region)}, 400

        except SQLAlchemyError as e:
         return {'message': e}, 500

     def get(self, name):
         region = RegionModel.find_by_name(name)
         if region:
             return jsonify(region.serialize())
         return {'message': 'region not found'}, 404
    
