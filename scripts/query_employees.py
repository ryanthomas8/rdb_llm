from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Employee
from app.config import config_by_name

# Load the correct configuration based on the environment
env = "dev_local"
config = config_by_name.get(env)
print(f"Using {env} configuration.")

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Query all employees
employees = session.query(Employee).all()
for employee in employees:
    print(employee.name, employee.birthday)