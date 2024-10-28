import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to save resources
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'  # Secret key for sessions

class DevelopmentConfig(Config):
    DEBUG = True  # Enable debug mode for development

class ProductionConfig(Config):
    DEBUG = False  # Disable debug mode for production
    # Add production-specific settings (e.g., database URI, logging)
