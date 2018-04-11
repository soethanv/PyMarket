from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    application = Flask(__name__)
    application.config.from_object(Config)

    db.init_app(application)
    migrate.init_app(application, db)

    return application

# this import must be below the application creation
# to prevent circular imports. routes uses the application variable
# from application import routes
from app.models import *
