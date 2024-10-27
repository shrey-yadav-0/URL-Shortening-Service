from flask import Flask
from app.extensions import init_extensions
from app.resources.status import status_bp
from app.resources.url_shortener import url_shortener_bp
from app.error_handler import register_error_handlers


def create_app(config_class):
    """Application factory that initializes and configures Flask app"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    init_extensions(app)

    # Register blueprints
    app.register_blueprint(status_bp)
    app.register_blueprint(url_shortener_bp)

    # Register error handlers
    register_error_handlers(app)

    return app
