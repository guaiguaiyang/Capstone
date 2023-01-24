from app import db
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    mane = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)