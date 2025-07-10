from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# PostgreSQL connection string
DatabaseURL = "postgresql://postgres:asif12345@localhost:5432/blogdb"

# Create the engine (DB connector)
engine = create_engine(DatabaseURL)
# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base class for models
Base = declarative_base()
# Dependency to get DB session in FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
