from flask import Blueprint, request, abort, jsonify, make_response
from app import db
from app.models.favorite import Favorite

favorite_bp = Blueprint("favorites", __name__, url_prefix="/favorites")

def get_one_obj_or_abort(cls, obj_id):
    try:
        obj_id = int(obj_id)
    except ValueError:
        response_str = f"Invalid ID: {obj_id}. ID must be an integer"
        abort(make_response(jsonify({"details":response_str}), 400))

    matching_obj = cls.query.get(obj_id)

    if not matching_obj:
        response_str = f"{cls.__name__} with id {obj_id} was not found in the database."
        abort(make_response(jsonify({"details":response_str}), 404))

    return matching_obj

# --------------------------  favorite Endpoints --------------------------
@favorite_bp.route("", methods=["POST"])
def create_a_favorite():
    request_body = request.get_json()
    new_favorite = Favorite.from_dict(request_body)

    if new_favorite.title is None or new_favorite.img is None:
        return jsonify({"details": "Invalid Favorite"}),400

    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({"favorite": new_favorite.to_dict()}), 201

@favorite_bp.route("", methods=["GET"])
def get_all_favorites():
    sort_param = request.args.get("sort")

    if sort_param == "desc":
        favorites = Favorite.query.order_by(Favorite.title.desc()).all()
    else:
        # favorites = favorite.query.all()
        favorites = Favorite.query.order_by(Favorite.title).all()

    response = [favorite.to_dict() for favorite in favorites]
    return jsonify(response), 200

@favorite_bp.route("/<id>", methods=["GET"])
def get_one_favorite_or_abort(id):
    # refactored:
    chosen_favorite = get_one_obj_or_abort(Favorite, id)
    favorite_dict = chosen_favorite.to_dict()

    if chosen_favorite.user_id:
        favorite_dict["user_id"] = chosen_favorite.user_id
    # try:
    #     id = int(id)
    # except ValueError:
    #     response_str = f"Invalid bike_id: `{id}`. ID must be an integer"
    #     abort(make_response(jsonify({"message":response_str}), 400))
    # matching_favorite = favorite.query.get(id)
    # if not matching_favorite:
    #     response_str = f"favorite with id `{id}` was not found in the database."
    #     abort(make_response(jsonify({"message":response_str}), 404))
    return jsonify({"favorite" : favorite_dict}), 200

@favorite_bp.route("/<id>", methods=["DELETE"])
def delete_one_favorite(id):
    chosen_favorite = get_one_obj_or_abort(Favorite, id)
    title = chosen_favorite.title

    db.session.delete(chosen_favorite)
    db.session.commit()

    return jsonify({"details": f'favorite {id} "{title}" successfully deleted'}), 200