
import datetime
import sqlite3
from database import db


#CREATE USERS
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # primary key
    username = db.Column(db.String(80), unique = True, nullable=False)
    email = db.Column(db.String(100), unique = True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable= False)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id"), unique=False, nullable=False)
    region = db.relationship("RegionModel", back_populates="users")
    # date_joined = db.Column(db.Date, default=datetime.utcnow)

    def __init__(self, username, email, password, region_id):
       self.username = username
       self.password = password
       self.email = email
       self.region_id = region_id
    

    def save_to_db(self):
        db.session.add(self)  #A session is a collection of object that we have to write to the db
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def serialize(self):
        return {
                "id": self.id,
                "username": self.username,
                "email": self.email,
                "region_id": self.region_id,
                'region': self.region
                }

    def delete_from_db(self):
         db.session.delete(self)
         db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id =_id).first()