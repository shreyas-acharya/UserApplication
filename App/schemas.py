from pydantic import BaseModel

class UserBase(BaseModel):
    fullname: str
    email: str
    age: int

class UserCreate(UserBase):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(UserBase):
    password: str

class User(UserBase):
    username: str

class Log(BaseModel):
    id: int
    username: str
    loggedin: bool
