from flask import Blueprint

# Define a Blueprint for this module (mchat)
sickbeatz = Blueprint('sickbeatz', __name__, url_prefix='/sickbeatz')

# Import all controllers
from controllers.users_controller import *
from controllers.songs_controller import *
from controllers.artists_controller import *
from controllers.likes_controller import *
