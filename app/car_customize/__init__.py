from flask import Blueprint

car_customize = Blueprint('car_customize', __name__)

from . import views