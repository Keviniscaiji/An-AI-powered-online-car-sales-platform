from flask import Flask, render_template
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
# moment = Moment()
babel = Babel()
db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO(cors_allowed_origins='*')
login_manager.login_view = 'auth.login'

def create_app(cfg_type: str):
    """
    Do initlization for flask application

    :param cfg_type: a string with content ('dev', 'test', 'release')
    :return: app: flask application to run
    """
    app = Flask(__name__)
    app.config.from_object(config[cfg_type])
    config[cfg_type].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
