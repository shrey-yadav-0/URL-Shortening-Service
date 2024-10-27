import traceback
from app.response import send_response


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(traceback.format_exc())
        error = dict()
        error["message"] = str(e)
        return send_response(
            status="error",
            message="Internal Server Error",
            errors=error,
            status_code=500
        )

    return app
