import os
import sys
import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


sys.path = ['', '..'] + sys.path[1:]

user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
host = os.environ.get('POSTGRES_HOST')
database = os.environ.get('POSTGRES_DB')
port = int(os.environ.get('POSTGRES_PORT'))

SQLALCHEMY_DATABASE_URL: str = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
