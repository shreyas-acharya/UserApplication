import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

username = os.environ.get("POSTGRES_USERNAME")
password = os.environ.get("POSTGRES_PASSWORD")
database = os.environ.get("POSTGRES_DATABASE")

URL = f"postgresql://{username}:{password}@postgresserver/{database}"
engine = create_engine(URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()
