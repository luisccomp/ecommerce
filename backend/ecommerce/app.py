from os import environ
from flask import Flask
from .extensions import db
from .exceptions import HttpError, handle_http_errors
from ecommerce import categories


def create_app():
    """Application factory function: it's recommended by official documentation fo launch an app this way"""
    app = Flask(__name__)
    app.config.from_mapping(environ.items())

    # Configuring and registering flask's extensions
    register_extensions(app)
    # Configuring application routes
    register_blueprings(app)

    app.register_error_handler(HttpError, handle_http_errors)

    return app


def register_extensions(app):
    """Register Flask extensions"""
    db.init_app(app)


def register_blueprings(app):
    """Register application routes"""
    app.register_blueprint(categories.api.blueprint)
