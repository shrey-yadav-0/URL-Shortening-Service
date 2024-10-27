import datetime
import hashlib


def generate_short_code(long_url):
    # Create a hash of the long URL
    hash_object = hashlib.sha256(long_url.encode())

    # Take the first 8 characters of the hash
    short_code = hash_object.hexdigest()[:8]

    return short_code


def get_current_time():
    return datetime.datetime.now(datetime.UTC).astimezone().replace(tzinfo=None)
