from flask import Blueprint, request, make_response, jsonify, abort
from app import db
from app.models.account import Account

account_bp = Blueprint("capstone", __name__, url_prefix="/user")
# check valid ID
def verify_user(user_id):
    try:
        user_id = int(user_id)
    except:
        abort(make_response({"message": 'Invalid user id'}, 400))

    user = Account.query.get(user_id)
    if not user:
        return abort(make_response({"message": 'User Not Found'}, 404))
    return user
# POST create user  
@account_bp.route("/signup", methods = ["POST"])
def create_user():
    request_body = request.get_json()
    if "email" not in request_body or "password" not in request_body:
        abort(make_response({"error":"invalid data need input email or password"},400))
    email = Account.query.filter_by(email = request_body["email"]).first()
    print(email)
    if email:
        abort(make_response({ "message": "user already exist" }, 409))
        db.session.rollback() 
    else:
        new_user = Account(
            name = request_body["name"],
            email = request_body["email"],
            password = request_body["password"],
        )
        db.session.add(new_user)
        db.session.commit()
        
    return make_response({
        "id":new_user.user_id,
        "name":new_user.name,
        "email":new_user.email
    },201)

# GET read all user info
@account_bp.route("", methods = ["GET"])
def read_all_user():
    users = Account.query.all()
    users_response = []
    for user in users:
        users_response.append({
            "id": user.user_id,
            "name": user.name,
            "email":user.email,
            "password":user.password
        })
    return jsonify(users_response)

#login
@account_bp.route("/login", methods = ["POST"])
def login():
    request_body = request.get_json()
    user = Account.query.filter_by(email = request_body["email"]).first()
    if not user: 
        return make_response({ "message": "User not found"}, 404)
    if user.password == request_body["password"]:
        return make_response({
            "email":user.email,
            "user_id":user.user_id
        })
    else:
        return make_response({ "message": "Password incorrect" }, 401)    

# Get a specific user   
@account_bp.route("/<user_id>", methods = ["GET"])
def get_one_user(user_id):
    user = verify_user(user_id)
    if user:
        return make_response(
            {"user":{"name": user.name,
            "email": user.email}},
            201)
    else: 
        return make_response({ "message": "user not found" }, 404)
