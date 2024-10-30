from app.resources.status import status_bp
from app.resources.url_shortener import url_shortener_bp


def register_blueprints(app):
    app.register_blueprint(status_bp)
    app.register_blueprint(url_shortener_bp)
