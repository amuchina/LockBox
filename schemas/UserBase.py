from pydantic import BaseModel
import os


class UserBase(BaseModel):
    username: str
    lockers_counter: int = 0


class UserCreate(UserBase):
    name: str or None = ""
    surname: str or None = ""
    password: str
    personal_user_salt: str = os.urandom(32).decode('latin1')


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
