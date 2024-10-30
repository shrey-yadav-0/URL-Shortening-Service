import datetime
import hashlib
from flask import abort
from app.extensions import mongo


class ShortURLModel:
    @staticmethod
    def create(data):
        # Check if there is no existing long URL
        existing_data = mongo.db.short_urls.find_one({"url": data["url"]})
        if existing_data:
            abort(400, description="This URL already exists")

        # Generate short code for long URL
        short_code = generate_short_code(data["url"])

        # Get current time in UTC
        now = get_current_time()

        # Insert the data
        data["short_code"] = short_code
        data["created_at"] = now
        data["updated_at"] = now
        data["access_count"] = 0
        mongo.db.short_urls.insert_one(data)

        # Manipulate the data to send it in response
        data["id"] = str(data["_id"])
        data.pop("_id")
        data.pop("access_count")

    @staticmethod
    def read(short_code, user_access=False, stats_required=False):
        collection_filter = {"short_code": short_code}
        project = {"_id": 0, "id": {"$toString": "$_id"}, "url": 1, "short_code": 1, "created_at": 1, "updated_at": 1}

        # Increase the count, whenever user tries to access it
        if user_access is True:
            mongo.db.short_urls.update_one(collection_filter, {"$inc": {"access_count": 1}})

        # Include 'access_count' in response whenever statistics are required
        if stats_required is True:
            project.update({"access_count": 1})

        # Check if data exists and return it
        data = mongo.db.short_urls.find_one(collection_filter, project)
        if not data:
            abort(404, description="No such short URL exist")
        return data

    @staticmethod
    def update(short_code, new_data):
        # Fetch old data
        old_data = ShortURLModel.read(short_code)

        # Check if there is no existing long URL
        existing_data = mongo.db.short_urls.find_one({"url": new_data["url"]})
        if existing_data:
            abort(400, description="This URL already exists")

        # Generate short code for long URL
        new_short_code = generate_short_code(new_data["url"])

        # Get current time in UTC
        now = get_current_time()

        # Update the data
        new_data["short_code"] = new_short_code
        new_data["updated_at"] = now
        mongo.db.short_urls.update_one({"short_code": short_code}, {"$set": new_data})

        # Manipulate the data to send it in response
        new_data["id"] = old_data["id"]
        new_data["created_at"] = old_data["created_at"]

    @staticmethod
    def delete(short_code):
        # Check if the data exists
        ShortURLModel.read(short_code)

        # Delete the data
        mongo.db.short_urls.delete_one({"short_code": short_code})


def generate_short_code(long_url):
    # Create a hash of the long URL
    hash_object = hashlib.sha256(long_url.encode())

    # Take the first 8 characters of the hash
    short_code = hash_object.hexdigest()[:8]

    return short_code


def get_current_time():
    return datetime.datetime.now(datetime.UTC).astimezone().replace(tzinfo=None)
