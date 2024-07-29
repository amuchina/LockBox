from sqlalchemy.orm import Session
from sqlalchemy import exc

from models.models import User
from schemas.UserBase import UserCreate

import os
import hashlib


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()  # type: ignore


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()  # type: ignore


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate, salt: bytes):
    if not salt:
        salt = os.urandom(32)
    try:
        hashed_password = hashlib.sha512()
        hashed_password.update(salt)
        hashed_password.update(user.password.encode())  # type: ignore
        hashed_password = hashed_password.hexdigest()
        new_user = User(username=user.username, hashed_password=hashed_password)  # type: ignore
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except exc.SQLAlchemyError as err:
        print(f"Error while creating user: {err}")
        return False
