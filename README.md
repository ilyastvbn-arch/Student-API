#  Student API

REST API for managing a student database, built with **FastAPI** + **SQLAlchemy** + **SQLite**.

##  Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM for database interaction
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [SQLite](https://www.sqlite.org/) — database
- [Uvicorn](https://www.uvicorn.org/) — ASGI server

##  Project Structure

```
school_project/
├── main.py          # API endpoints
├── database.py      # Database connection
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
└── requirements.txt
```

##  Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/ilyastvbn-arch/Student-API.git
cd Student-API
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
uvicorn main:app --reload
```

Server will run at `http://localhost:8000`

##  Endpoints

| Method  |       URL        |      Description       |
|-------- |------------------|
| `GET`   | `/students/`     | Get all students       |
| `POST`  | `/students/`     | Create a new student   |
| `GET`   | `/students/{id}` | Get a student by ID    |
| `DELETE`| `/students/{id}` | Delete a student by ID |

##  Student Model

| Field         |Type |             Description             |
|---------------|-----|-------------------------------------|
| `id`          | int | Unique identifier (auto-generated)  |
| `name`        | str | First name                          |
| `surname`     | str | Last name                           |
| `age`         | int | Age                                 |
| `entry_year`  | int | Year of enrollment                  |
| `email`       | str | Email (unique)                      |

##  API Documentation

Once the server is running, interactive docs are available at:

- **Swagger UI** → `http://localhost:8000/docs`
- **ReDoc** → `http://localhost:8000/redoc`

##  Example Request

Create a student:
```bash
curl -X POST "http://localhost:8000/students/" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "John",
           "surname": "Doe",
           "age": 18,
           "entry_year": 2024,
           "email": "john@example.com"
         }'
```
