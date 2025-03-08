import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.models import User
from app.config import config_by_name

# Get the environment
env = os.environ.get('APP_ENV', 'dev')  

# Load the correct configuration based on the environment
config = config_by_name.get(env)
print(f"Using {env} configuration.")

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
sample_users = [
    User(name="John Doe", description="A description for John", birthday=datetime(1990, 5, 1)),
    User(name="Jane Smith", description="A description for Jane", birthday=datetime(1992, 7, 15)),
    User(name="Alice Brown", description="A description for Alice", birthday=datetime(1985, 9, 25)),
]

# Add the sample data to the session
session.add_all(sample_users)

# Commit the session to save the data to the database
session.commit()

# Close the session
session.close()

print("Sample data inserted successfully!")
