from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.favorite import Favorite

favorite_bp = Blueprint("favorites", __name__, url_prefix="/favorites")