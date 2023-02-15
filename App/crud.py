from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, username: str):
    return db.query(models.User).get(username)

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, username: str, new_info: schemas.UserUpdate):
    info = get_user(db, username)
    info.password = new_info.password
    info.email = new_info.email
    info.age = new_info.age
    info.fullname = new_info.fullname
    
    db.commit()
    db.refresh(info)

    return info

def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()
    return 

def add_log(db: Session, log: schemas.Log):
    new_log = models.Log(**log.dict())
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

def get_latest_log(db:Session):
    obj = db.query(models.Logs).order_by(models.Logs.id.desc()).first()
    return obj
