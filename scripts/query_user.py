import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User
from config import config_by_name

# Get the environment
env = os.environ.get('APP_ENV', 'dev')  

# Load the correct configuration based on the environment
config = config_by_name.get(env)
print(f"Using {env} configuration.")

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Query all users
users = session.query(User).all()
for user in users:
    print(user.name, user.birthday)