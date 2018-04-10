from flask import Flask

app = Flask(__name__)


# this import must be below the app creation
# to prevent circular imports. routes uses the app variable
from app import routes
