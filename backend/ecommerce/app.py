from os import environ

from flask import Flask

from . import exceptions
from .controllers import categories_controller
from .extensions import db, migrate
from .settings import profiles
from .commands import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(profiles.get(environ.get('FLASK_ENV'), 'development'))

    register_extensions(app)
    register_exception_handlers(app)

    app.register_blueprint(categories_controller.router)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_exception_handlers(app):
    app.register_error_handler(exceptions.BaseHttpException, exceptions.handle_base_http_exception)
