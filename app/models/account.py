from app import db

class Account(db.Model):
    user_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    favorites = db.relationship("Favorite", back_populates="account")

