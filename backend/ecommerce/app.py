from os import environ
from flask import Flask
from .extensions import db, bcrypt, jwt
from .exceptions import HttpError, handle_http_errors
from ecommerce import categories, products, users


def create_app():
    """Application factory function: it's recommended by official documentation fo launch an app this way"""
    app = Flask(__name__)
    app.config.from_mapping(environ.items())
    app.config['JSON_SORT_KEYS'] = False

    # Configuring and registering flask's extensions
    register_extensions(app)
    # Configuring application routes
    register_blueprints(app)

    app.register_error_handler(HttpError, handle_http_errors)

    return app


def register_extensions(app):
    """Register Flask extensions"""
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    """Register application routes"""
    app.register_blueprint(categories.api.blueprint)
    app.register_blueprint(products.api.blueprint)
    app.register_blueprint(users.api.blueprint)
