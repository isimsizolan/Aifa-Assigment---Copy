from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import get_settings
from app.utils.errors import DatabaseException

# Database initialization for SQLAlchemy for intended use with Repository pattern
# This code initializes a SQLAlchemy engine and session factory for PostgreSQL


settings = get_settings()

try:
    engine = create_engine(settings.postgres_url, echo=False)
    SessionLocal = sessionmaker(bind=engine)
except Exception as e:
    raise DatabaseException(f"Failed to initialize database connection: {str(e)}")

def get_session():
    return SessionLocal()