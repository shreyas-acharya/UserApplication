from .database import Base
from sqlalchemy import String, Integer, Column

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String),
    fullname = Column(String),
    email = Column(String, unique=True, index=True)
    age = Column(Integer),
