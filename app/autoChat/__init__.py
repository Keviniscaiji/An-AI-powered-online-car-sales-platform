from flask import Blueprint

autoChat = Blueprint('autoChat', __name__)

from . import views