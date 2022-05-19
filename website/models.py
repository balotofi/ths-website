
# from os import access

from sqlalchemy import Column
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_ = db.Column(db.String(20))
    subject = db.Column(db.String(20))
    score = db.Column(db.String(20))
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    pupil_id = db.Column(db.Integer, db.ForeignKey('pupil.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    userName = db.Column(db.String(150), unique=True)
    familyName = db.Column(db.String(150))
    accessType = db.Column(db.String(10))
#one to many relationship i.e one user can have many pupils
    pupils = db.relationship('Pupil') 


class Pupil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150))
    familyName = db.Column(db.String(150))
    class_ = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#one to many relationship i.e one pupil has many results
    results = db.relationship('Result') 

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
#many to one relationship i.e many pupils have one teacher