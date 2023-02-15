from .database import Base
from sqlalchemy import String, Integer, Column, Boolean, DateTime

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String),
    fullname = Column(String),
    email = Column(String, unique=True, index=True)
    age = Column(Integer)

class Logs(Base):
    __tablename__ = "logs"
    id = Column(Integer, priary_key=True, index=True)
    username = Column(String, index=True)
    loggedin = Column(Boolean)
