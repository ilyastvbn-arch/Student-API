from fastapi import Depends, FastAPI, HTTPException, Path
from typing import Optional, List, Dict, Annotated
from sqlalchemy.orm import Session

from database import Base, engine, session_local
from models import Student
from schemas import StudentCreate, Student as Student_db

# Create the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)
def get_db():
    # Dependency function to get a database session for each request,
    # ensuring that the session is properly closed after the request is processed.
    db = session_local()
    try: #
        yield db
    finally:
        db.close()
        
### Define the API endpoints
@app.get("/students/", response_model=List[Student_db])
def list_students(db: Session = Depends(get_db)) -> List[Student_db]:
    """Get a list of all students in the database."""
    
    return db.query(Student).all() # Query the database for all students and return them as a list

@app.post("/students/", response_model= Student_db)
def create_student(student: StudentCreate, db: Session = Depends(get_db)) -> Student:
    """Create a new student in the database."""
    
    # Create a new Student instance using the data from the request body
    db_student = Student(name=student.name,             
                         surname=student.surname, 
                         age=student.age, 
                         entry_year=student.entry_year, 
                         email=student.email)
    db.add(db_student)      # Add the new student to the database session
    db.commit()             # Commit the transaction to save the student in the database
    db.refresh(db_student)  # Refresh the instance to get the generated ID and any other database defaults
    return db_student

@app.delete("/students/{student_id}")
def delete_student(student_id: Annotated[int, Path(title="Here input student ID", ge=1)],
                   db: Session = Depends(get_db)):
    """Delete a student from the database by their ID."""
    
    # Query the database for the student with the specified ID
    student = db.query(Student).filter(Student.id == student_id).first() 
    if student is None:
        return HTTPException(status_code=404, detail="User not found") # If the student does not exist, return a 404 error
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}

@app.get("/students/{student_id}", response_model=Student_db)
def get_student(student_id: Annotated[int, Path(title="Here input student ID")],
                db: Session = Depends(get_db)) -> Student:
    """Get a student from the database by their ID."""
    
    # Query the database for the student with the specified ID
    student = db.query(Student).filter(Student.id == student_id).first() 
    if student is None:
        return HTTPException(status_code=404, detail="User not found")
    return student