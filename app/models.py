from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    DECIMAL,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship, declarative_base

# Define the base class for your models
Base = declarative_base()


# Define the 'department' table
class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)

    # Relationship to employee
    employee = relationship("Employee", back_populates="department")


# Define the 'employee' table
class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    birthday = Column(Date, nullable=True)
    department_id = Column(Integer, ForeignKey("department.id", ondelete="SET NULL"))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    department = relationship("Department", back_populates="employee")
    salary = relationship("Salary", back_populates="employee")
    project = relationship("EmployeeProject", back_populates="employee")


# Define the 'salary' table
class Salary(Base):
    __tablename__ = "salary"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    employee_id = Column(Integer, ForeignKey("employee.id", ondelete="CASCADE"))
    salary = Column(DECIMAL(10, 2), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)

    # Relationship
    employee = relationship("Employee", back_populates="salary")


# Define the 'project' table
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    budget = Column(DECIMAL(12, 2), nullable=False)

    # Relationship to employee-project
    employee = relationship("EmployeeProject", back_populates="project")


# Define the 'employee_projects' table (many-to-many)
class EmployeeProject(Base):
    __tablename__ = "employee_projects"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    employee_id = Column(Integer, ForeignKey("employee.id", ondelete="CASCADE"))
    project_id = Column(Integer, ForeignKey("project.id", ondelete="CASCADE"))
    role = Column(String(50), nullable=False)

    # Relationships
    employee = relationship("Employee", back_populates="project")
    project = relationship("Project", back_populates="employee")
