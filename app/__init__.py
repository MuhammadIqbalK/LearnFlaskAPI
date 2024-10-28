from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Load config
    db.init_app(app)

    with app.app_context():
        from .routes import register_routes  # Import the register function
        register_routes(app)  # Register routes
        db.create_all()  # Create database tables if needed

    return app
