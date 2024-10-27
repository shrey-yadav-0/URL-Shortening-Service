from flask import Blueprint, request
from flask_restful import Api, Resource
from app.models.url_shortener import ShortURLModel
from app.response import send_response

url_shortener_bp = Blueprint("url_shortener", __name__)
url_shortener_api = Api(url_shortener_bp)


class ShortURL(Resource):
    def get(self, short_code):
        # Fetch data
        data = ShortURLModel.read(short_code, user_access=True)

        # Return response
        return send_response(
            status="success",
            message="Original URL retrieved",
            data=data,
            status_code=200
        )

    def post(self):
        # Extract payload
        data = {
            "url": request.json["url"]
        }

        # Insert data
        ShortURLModel.create(data)

        # Return response
        return send_response(
            status="success",
            message="Short URL created",
            data=data,
            status_code=201
        )

    def put(self, short_code):
        # Extract payload
        data = {
            "url": request.json["url"]
        }

        # Update data
        ShortURLModel.update(short_code, data)

        # Return response
        return send_response(
            status="success",
            message="Short URL updated",
            data=data,
            status_code=200
        )

    def delete(self, short_code):
        # Delete data
        ShortURLModel.delete(short_code)

        # Return response
        return send_response(
            status="success",
            status_code=204
        )


class URLStatistics(Resource):
    def get(self, short_code):
        # Fetch data
        data = ShortURLModel.read(short_code, stats_required=True)

        # Return response
        return send_response(
            status="success",
            message="URL statistics retrieved",
            data=data,
            status_code=200
        )


url_shortener_api.add_resource(ShortURL, "/shorten", "/shorten/<short_code>")
url_shortener_api.add_resource(URLStatistics, "/shorten/<short_code>/stats")
