from app import db

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user_id"))
    user = db.relationship("UserAccount", back_populates = "favorites")