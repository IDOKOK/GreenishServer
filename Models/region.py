
import datetime
import sqlite3
from database import db


#CREATE USERS
class RegionModel(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)  # primary key
    name_of_region = db.Column(db.String(80), unique = True, nullable=False)
    users = db.relationship("UserModel", back_populates="region", lazy="dynamic") #dynamic means populating the users only when you tell it to.
    # date_joined = db.Column(db.Date, default=datetime.utcnow)

    def __init__(self, name_of_region):
       self.name_of_region = name_of_region


    def serialize(self):
        return {
                "id": self.id,
                "name_of_region": self.name_of_region
                # "users": self.users
                }

    def save_to_db(self):
        db.session.add(self)  #A session is a collection of object that we have to write to the db
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name_of_region = name).first()