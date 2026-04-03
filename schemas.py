from pydantic import BaseModel

# Define the schemas for the API logic  
class StudentBase(BaseModel):
    name: str
    surname: str
    age: int
    entry_year: int
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    
    # This allows Pydantic to read data from SQLAlchemy models using attribute access.
    model_config = {"from_attributes": True}  


