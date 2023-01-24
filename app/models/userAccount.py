from app import db

class UserAccounts(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    favorites = db.relationship("Favorite", back_populates = "userAccount")