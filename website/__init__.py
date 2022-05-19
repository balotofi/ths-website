from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bbdgw584'
    # Old SQLite DB
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # New MySQL DB
    #app.config['SQLALCHEMY_DATABASE_URI', SQL_ALCHEMY_TRACK_MODIFICATIONS == True] = f'mysql://username:password@localhost/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # from . import models
    from .models import User, Result, Pupil

    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
