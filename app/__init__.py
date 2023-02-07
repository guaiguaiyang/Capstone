from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS



db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
  

    from app.models.account import Account
    from app.models.favorite import Favorite
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes.account_routes import account_bp
    app.register_blueprint(account_bp)
    from .routes.favorite_routes import favorite_bp
    app.register_blueprint(favorite_bp)
    
    CORS(app)
    return app