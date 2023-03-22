from flask import Blueprint

auth = Blueprint('imgSearch', __name__)

from . import views