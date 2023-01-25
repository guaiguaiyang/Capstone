from app import db

class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

