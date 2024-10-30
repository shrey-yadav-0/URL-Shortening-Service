from flask import Flask
from app.blueprints import register_blueprints
from app.config import Config
from app.extensions import init_extensions
from app.error_handler import register_error_handlers


def create_app():
    """Application factory that initializes and configures Flask app"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    init_extensions(app)

    # Register blueprints
    register_blueprints(app)

    # Register error handlers
    register_error_handlers(app)

    return app
