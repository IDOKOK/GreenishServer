from flask import abort, jsonify   # https://flask.palletsprojects.com/en/2.2.x/
from flask_restful import request, reqparse
 
from Models import RegionModel
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError  # error when violating foreignkey/primary integrity

from schemas import RegionSchema   #https://docs.sqlalchemy.org/en/20/core/exceptions.html


blp = Blueprint("region", __name__, description="Operations on region")

@blp.route("/region")
class Region(MethodView):
     @blp.arguments(RegionSchema)
     @blp.response(200, RegionSchema)
     def post(self, region_data):
        try:
         region = RegionModel(**region_data)  # call regionModel constructor
         region.save_to_db()    # save to the database through the model
         return region  # turn the region object to json

        # except IntegrityError:                  
        #  return {'message': "A region with name '{}' already exists.". format(region.name_of_region)}, 400

        except IntegrityError:
            abort(400, message= "Error in data inconsitency ! your name_of_region has to be unique" )

        except SQLAlchemyError:
            abort(500, message= "An error occurred while adding the region" )

     @blp.response(200, RegionSchema(many=True))
     def get(self):
         region = RegionModel.find_by_name(name)
         if region:
             return jsonify(region.serialize())
         return {'message': 'region not found'}, 404
    

@blp.route("/region/all")
class RegionList(MethodView):
    @blp.response(200, RegionSchema(many=True))
    def get(self):
        regions = RegionModel.findAll()
        return regions

