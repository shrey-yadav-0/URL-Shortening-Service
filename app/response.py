from flask import jsonify, make_response


def send_response(status, message=None, data=None, errors=None, status_code=200):
    response_body = {
        "status": status,
        "message": message,
        "data": data,
        "errors": errors     # Additional error details if any
    }
    # Remove keys with `None` values for a cleaner response
    response_body = {k: v for k, v in response_body.items() if v is not None}
    return make_response(jsonify(response_body), status_code)
