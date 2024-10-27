from flask import Blueprint
from app.extensions import mongo

status_bp = Blueprint("status", __name__)


@status_bp.route('/application-status')
def application_status():
    return "URL Shortening Service is running successfully."


@status_bp.route('/database-connection-status')
def database_connection_status():
    try:
        mongo.cx.admin.command('ping')  # Ping MongoDB
        status = "MongoDB is connected."
    except Exception as e:
        status = f"Database connection failed: {str(e)}"
    return status
