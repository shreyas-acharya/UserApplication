from database import Base
from sqlalchemy import String, Integer, Column, Boolean, Identity

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)

class Logs(Base):
    __tablename__ = "logs"
    id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    username = Column(String, index=True)
    loggedin = Column(Boolean)
