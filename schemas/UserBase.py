from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    lockers_counter: int = 0


class UserCreate(UserBase):
    password: str
    personal_user_salt: bytes or None = None


class User(UserBase):
    id: int
    name: str or None = None
    surname: str or None = None

    class Config:
        from_attributes = True
