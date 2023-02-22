from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    fullname: str
    email: str
    age: int


class UserList(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserUpdate(BaseModel):
    password: Optional[str] = None
    fullname: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None


class User(UserBase):
    username: str

    class Config:
        orm_mode = True


class Log(BaseModel):
    id: int
    username: str
    loggedin: bool

    class Config:
        orm_mode = True
