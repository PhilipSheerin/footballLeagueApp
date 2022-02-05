from os import path
import sqlite3
from flask import Flask

#Define DB connection
db = sqlite3.connect('database.db', check_same_thread=False)
DB_NAME = "database.db"


def create_app():

    #Following is run when main.py is run
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ''
    app.config['SQLITE_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    #Set up blueprints
    from .views import views
    from .api import apiView

    #Connect to main site views
    app.register_blueprint(views, url_prefix='/')

    #Connect to API views
    app.register_blueprint(apiView, url_prefix='/api')

    return app