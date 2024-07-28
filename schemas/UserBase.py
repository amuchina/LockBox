from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    lockers_counter: int = 0


class UserCreate(UserBase):
    password: str
    personal_user_salt: str = None


class User(UserBase):
    id: int
    name: str = None
    surname: str = None

    class Config:
        orm_mode = True
