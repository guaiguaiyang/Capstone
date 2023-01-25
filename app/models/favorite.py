from app import db

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('account.user_id'))
    account = db.relationship("Account", back_populates="favorites")
    