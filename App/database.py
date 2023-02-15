import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
database = os.getenv("POSTGRES_DB")

URL = f"postgresql://{username}:{password}@db:5432/{database}"
engine = create_engine(URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()
