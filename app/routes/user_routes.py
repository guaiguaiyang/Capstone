from flask import Blueprint, request, make_response, jsonify, abort
from app import db
from app.models.userAccount import UserAccount

capstone_bp = Blueprint("capstone", __name__, url_prefix="/users")

# POST create user info 
@capstone_bp.route("/signup", methods = ["POST"])
def create_user():
    request_body = request.get_json()
    if "email" not in request_body or "password" not in request_body:
        abort(make_response({"error":"invalid data need input email or password"},400))
    new_user = UserAccount(
        name = request_body["name"],
        email = request_body["email"],
        password = request_body["password"],
    )
    db.session.add(new_user)
    db.session.commit()
    
    return make_response({
        "id":new_user.id,
        "name":new_user.name,
        "email":new_user.email
    },201)

# GET read all user info
@capstone_bp.route("", methods = ["GET"])
def read_all_user():
    users = UserAccount.query.all()
    users_response = []
    for user in users:
        users_response.append({
            "id": user.id,
            "name": user.name,
            "email":user.email,
            "password":user.password
        })
    return jsonify(users_response)

#login
@capstone_bp.route("/login", methods = ["POST"])
def login():
    request_body = request.get_json()
    user = UserAccount.query.filter_by(email = request_body["email"]).first()
    if not user: 
        return make_response({ "message": "User not found"}, 404)
    if user.password == request_body["password"]:
        return make_response({
            "email":user.email,
            "user_id":user.user_id
        })
    else:
        return make_response({ "message": "Password incorrect" }, 401)
# check valid ID
def verify_user(user_id):
    try:
        user_id = int(user_id)
    except:
        abort(make_response({"message": 'Invalid user id'}, 400))

    user = UserAccount.query.get(user_id)
    if not user:
        return abort(make_response({"message": 'User Not Found'}, 404))
    return user

# Get a specific user   
@capstone_bp.route("/<user_id>", methods = ["GET"])
def get_user(user_id):
    user = verify_user(user_id)
    return make_response(
        {"name": user.name,
         "email": user.email}, 
        201)
