from sqlalchemy import Column, Integer, String, DateTime, Unicode
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for your models
Base = declarative_base()

# Define the 'user' table as a model class
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Unicode)
    birthday = Column(DateTime)
