from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Define the Student model of the database
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    age = Column(Integer)
    entry_year = Column(Integer)
    email = Column(String, unique=True, index=True)
    
