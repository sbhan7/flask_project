import os
from test_app import app
from test_app import db



# class ORM like django
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    
# FOR ONCE YOU CREATE THE DATABASE
# db.create_all()