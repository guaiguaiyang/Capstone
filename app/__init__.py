from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
  
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    from app.models.userAccount import UserAccounts
    from app.models.favorite import Favorites
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes.user_routes import capstone_bp
    app.register_blueprint(capstone_bp)
    
    return app