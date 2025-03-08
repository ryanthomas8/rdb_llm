import os

# Base configuration class
class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Development environment configuration
class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_DEV') or \
        'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/mydatabase_dev'

# Testing environment configuration
class TestingConfig(Config):
    """Testing environment configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST') or \
        'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/mydatabase_test'

# Production environment configuration
class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_PROD') or \
        'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/mydatabase_prod'

# Choosing the right environment
config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}
