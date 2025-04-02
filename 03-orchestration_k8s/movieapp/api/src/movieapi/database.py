import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = f"postgresql+psycopg2://{
    os.environ['DB_USER']
    }:{
        os.environ['DB_PASSWORD']
    }@{
        os.environ['DB_HOST']
    }:{
        os.environ['DB_PORT']
    }/{
        os.environ['DB_DBNAME']
    }"

engine = create_engine(
    DATABASE_URL,
    echo=True # debug SQL queries
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
