from sqlalchemy.orm import Session
from sqlalchemy import exc

from models.models import User
from schemas.UserBase import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()  # type: ignore


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()  # type: ignore


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    try:
        new_user = User(name=user.name, surname=user.surname, username=user.username, hashed_password=user.password, personal_user_salt=user.personal_user_salt)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except exc.SQLAlchemyError as err:
        print(f"Error while creating user: {err}")
        return False
