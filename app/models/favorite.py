from app import db

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    recipe_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('account.user_id'))
    account = db.relationship("Account", back_populates="favorites")
    
    def to_dict(self):
        favorite_dict = {
            "id": self.id,
            "title": self.title,
            "img": self.img,
        }
        return favorite_dict
    
    @classmethod
    def from_dict(cls, obj_dict):
        new_obj = cls(
            title = obj_dict.get("title", None),
            img = obj_dict.get("img", None),
            )
        return new_obj