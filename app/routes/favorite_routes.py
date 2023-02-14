from flask import Blueprint, request, abort, jsonify, make_response
from app import db
from app.models.favorite import Favorite

favorite_bp = Blueprint("favorites", __name__, url_prefix="/favorites")
# POST create new favorit
@favorite_bp.route("/<user_id>", methods=["POST"])
def create_favorit(user_id):
    request_body = request.get_json()
    if "title" not in request_body or "image" not in request_body:
        return jsonify({"message": "Title and image must be specified."}, 400)
    new_favorit = Favorite(
        title = request_body["title"],
        image = request_body["image"],
        recipe_id = request_body["recipe_id"],
        user_id = user_id
    )
    db.session.add(new_favorit)
    db.session.commit()
    return make_response(jsonify({"title":new_favorit.title,"user_id":new_favorit.user_id,"recipe_id":new_favorit.recipe_id}),201)
@favorite_bp.route("/<fav_id>", methods=["DELETE"])
def delete_fav(fav_id):
    fav = Favorite.query.get(fav_id)
    db.session.delete(fav)
    db.session.commit()
    return make_response(f"#{fav_id} successfully deleted", 200)

