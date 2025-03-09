from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from app.models import Department, Employee, Salary, Project, EmployeeProject
from app.config import config_by_name

# Load the correct configuration based on the environment
env = "dev_local"
config = config_by_name.get(env)
print(f"Using {env} configuration.")

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Clear tables (optional, useful for testing)
session.query(EmployeeProject).delete()
session.query(Salary).delete()
session.query(Employee).delete()
session.query(Project).delete()
session.query(Department).delete()
session.commit()

# Create sample departments
departments = [
    Department(name="Engineering"),
    Department(name="Marketing"),
    Department(name="Sales"),
]
session.add_all(departments)
session.commit()

# Fetch department IDs
engineering = session.query(Department).filter_by(name="Engineering").first()
marketing = session.query(Department).filter_by(name="Marketing").first()
sales = session.query(Department).filter_by(name="Sales").first()

# Create sample employees
employees = [
    Employee(name="John Doe", birthday=date(1990, 5, 1), department=engineering),
    Employee(name="Jane Smith", birthday=date(1992, 7, 15), department=marketing),
    Employee(name="Alice Brown", birthday=date(1985, 9, 25), department=sales),
]
session.add_all(employees)
session.commit()

# Fetch employee IDs
john = session.query(Employee).filter_by(name="John Doe").first()
jane = session.query(Employee).filter_by(name="Jane Smith").first()
alice = session.query(Employee).filter_by(name="Alice Brown").first()

# Create sample salaries
salaries = [
    Salary(employee=john, salary=80000, start_date=date(2020, 1, 1), end_date=None),
    Salary(employee=jane, salary=70000, start_date=date(2021, 3, 1), end_date=None),
    Salary(employee=alice, salary=90000, start_date=date(2019, 6, 1), end_date=None),
]
session.add_all(salaries)
session.commit()

# Create sample projects
projects = [
    Project(name="AI Research", budget=500000),
    Project(name="Marketing Campaign", budget=200000),
]
session.add_all(projects)
session.commit()

# Fetch project IDs
ai_research = session.query(Project).filter_by(name="AI Research").first()
marketing_campaign = session.query(Project).filter_by(name="Marketing Campaign").first()

# Assign employees to projects
employee_projects = [
    EmployeeProject(employee=john, project=ai_research, role="Developer"),
    EmployeeProject(employee=jane, project=marketing_campaign, role="Marketer"),
    EmployeeProject(employee=alice, project=ai_research, role="Data Scientist"),
]
session.add_all(employee_projects)
session.commit()

# Close the session
session.close()

print("Sample data inserted successfully!")
