
from os import access
from . import db
from flask_login import UserMixin
# from sqlalchemy.sql import func


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    userName = db.Column(db.String(150), unique=True)
    familyName = db.Column(db.String(150))
    accessType = db.Column(db.String(10))
    # notes = db.relationship('Note') 