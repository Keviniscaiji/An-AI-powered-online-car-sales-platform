from flask import Blueprint

carCostumize = Blueprint('carCostumize', __name__)

from . import views