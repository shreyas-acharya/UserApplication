from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, username: str):
    return db.query(models.User).get(username)

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    check = get_user(db, user.username)
    if check is not None:
        print("Username already exists")
        return 
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, username: str, new_info: schemas.UserUpdate):
    info = get_user(db, username)
    
    if info is None:
        print("User doesn't exists")
        return
    
    info.password = new_info.password
    info.email = new_info.email
    info.age = new_info.age
    info.fullname = new_info.fullname
    
    db.commit()
    db.refresh(info)

    return info

def delete_user(db: Session, username: str):
    check = get_user(db, username)

    if check is None:
        print("User doesn't exist")
        return

    db.delete(check)
    db.commit()
    return 
