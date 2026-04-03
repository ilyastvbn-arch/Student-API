from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_BD_URL = "sqlite:///./test.db"

# Create the database engine
engine = create_engine(SQL_BD_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our models
Base = declarative_base()