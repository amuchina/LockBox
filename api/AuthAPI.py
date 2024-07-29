from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database.LockBoxDBManager import SessionLocal, dbengine

from dbcrud.users import UserController
from schemas.UserBase import UserBase
from schemas.UserBase import UserCreate
AuthAPI = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@AuthAPI.post("/login")
def read():
    return {}


@AuthAPI.post("/register", response_model=UserBase)
def register(user: UserCreate, db_session: Session = Depends(get_db)):
    new_user = UserController.get_user_by_username(db_session, username=user.username)
    if new_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return UserController.create_user(db=db_session, user=user, salt=user.personal_user_salt)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(AuthAPI, port=8080)
