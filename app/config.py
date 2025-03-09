import os

# Development environment configuration
class DevelopmentConfig():
    """Development environment configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_DEV') or \
        'postgresql+psycopg2://postgres:mysecretpassword@postgres:5432/postgres'
    
# Development Local environment configuration
class DevelopmentLocalConfig():
    """Development environment configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_DEV_LOCAL') or \
        'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres'

# Testing environment configuration
class TestingConfig():
    """Testing environment configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST') or \
        'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres'

# Production environment configuration
class ProductionConfig():
    """Production environment configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_PROD') or \
        'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres'

# Choosing the right environment
config_by_name = {
    'dev': DevelopmentConfig,
    'dev_local': DevelopmentLocalConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}
