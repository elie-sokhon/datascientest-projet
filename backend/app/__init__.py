import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env
load_dotenv()

# Global extensions
db = SQLAlchemy()
socketio = SocketIO()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Basic config
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lobby.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    with app.app_context():
        from app.models import Message, User

    # Register blueprints
    from app.routes.user_routes import user_bp

    app.register_blueprint(user_bp)

    from app.routes import socketio_events  # Import to register events

    return app
