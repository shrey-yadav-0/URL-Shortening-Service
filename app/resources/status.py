import os
from flask import Blueprint
from app.extensions import mongo

status_bp = Blueprint("status", __name__)


@status_bp.route('/application-status')
def application_status():
    return "URL Shortening Service is running successfully."


@status_bp.route('/database-connection-status')
def database_connection_status():
    try:
        database_list = mongo.cx.list_database_names()
        database_name = os.getenv("MONGO_URI").split('/')[-1]
        if database_name in database_list:
            status = f"{database_name} is connected."
        else:
            status = f"{database_name} is not connected."
    except Exception as e:
        status = f"Database connection failed: {str(e)}"
    return status
