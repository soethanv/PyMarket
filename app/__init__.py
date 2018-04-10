from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


# this import must be below the app creation
# to prevent circular imports. routes uses the app variable
from app import routes
