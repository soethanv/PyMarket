from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from importlib import import_module
from config import Config
from views.helper import all_blueprints

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    application = Flask(__name__)
    application.config.from_object(Config)

    # initialize models
    from models.helper import model_classes

    # initialize blueprints
    for bp in all_blueprints:
        import_module(bp.import_name)
        application.register_blueprint(bp)


    db.init_app(application)
    migrate.init_app(application, db)

    return application
