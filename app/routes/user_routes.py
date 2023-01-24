from flask import Blueprint
capstone_bp = Blueprint("capstone", __name__, url_prefix="/users")

@capstone_bp.route("", methods = ["GET"])
def say_hello_world():
    response_body = "Hello, World!"
    return response_body, 201
