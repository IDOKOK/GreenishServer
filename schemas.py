from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    id= fields.Int(dump_only=True)  # We just want to return the id and not pass it through the request
    username = fields.Str(required=True)   # We want to receive it in the payload
    email = fields.Str(required=True)
    password =  fields.Str(required=True)
   
class UserUpdateSchema(Schema):
    username = fields.Str()  # having () without any arguments means its not required
    email = fields.Str()
    password =  fields.Str()
    region_id = fields.Int()

class PlainRegionSchema(Schema):
    id= fields.Int(dump_only=True)  # We just want to return the id and not pass it through the request
    name_of_region = fields.Str(required=True)   # We want to receive it in the payload


class UserSchema(PlainUserSchema):
    region_id = fields.Int(required=True, load_only=True)
    region = fields.Nested(PlainRegionSchema(), dump_only=True) # return only the objects of the region that belongs to many users

class RegionSchema(PlainRegionSchema):
    users = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)
    
