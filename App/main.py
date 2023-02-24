from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn

import utils.crud as crud
import utils.models as models
import utils.schemas as schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def user_logged_in(db):
    last_login = crud.get_latest_log(db)
    if last_login is None or last_login.loggedin == False:
        return None
    return last_login.username


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def ping():
    return "User Application is running"


@app.get("/getDetails")
def get_user(db: Session = Depends(get_db)):
    prev_user = user_logged_in(db)
    if prev_user is None:
        return HTTPException(status_code=401, detail="No user logged in!!!")
    return crud.get_user(db, prev_user)


@app.get("/getUsers", response_model=list[schemas.UserList])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.post("/addUser")
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    check = crud.get_user(db, user.username)
    if check is not None:
        return HTTPException(status_code=402, detail="Username already exists!!!")
    return crud.create_user(db, user)


@app.patch("/updateUser")
def update(user: schemas.UserUpdate, db: Session = Depends(get_db)):
    prev_user = user_logged_in(db)
    if prev_user is None:
        return HTTPException(status_code=401, detail="No user logged in!!!")
    crud.update_user(db, prev_user, user)
    return "User Information Updated"


@app.delete("/deleteUser")
def delete(db: Session = Depends(get_db)):
    prev_user = user_logged_in(db)
    if prev_user is None:
        return HTTPException(status_code=401, detail="No user logged in!!!")
    logout(db)
    return crud.delete_user(db, crud.get_user(db, prev_user))


@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    check = crud.get_user(db, user.username)
    if check is None:
        return HTTPException(status_code=403, detail="User doesn't exits")
    if check.password != user.password:
        return HTTPException(status_code=404, detail="Incorrect password")

    prev_user = user_logged_in(db)
    new_log = models.Logs(username=user.username, loggedin=True)
    if prev_user is None:
        crud.add_log(db, new_log)
        return f"Login Successful : {user.username}"
    else:
        if prev_user == new_log.username:
            return f"Already logged in"
        logout(db)
        crud.add_log(db, new_log)
        return f"Logout : {prev_user}   Login Successful : {user.username}"


@app.post("/logout")
def logout(db: Session = Depends(get_db)):
    prev_user = user_logged_in(db)
    if prev_user is None:
        return "No user logged in!!!"
    else:
        new_log = models.Logs(username=prev_user, loggedin=False)
        crud.add_log(db, new_log)
        return f"Logout Successful : {prev_user}"


@app.get("/getLogs", response_model=list[schemas.Log])
def get_logs(db: Session = Depends(get_db)):
    return crud.get_logs(db)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")
