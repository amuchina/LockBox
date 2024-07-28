from LockBoxDBManager import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Locker


class User(BaseModel):

    __tablename__ = "users"

    uuid: UUID = uuid4()
    id = Column(Integer, primary_key=True)
    name: Optional[str] = Column(String, index=True, nullable=True)
    surname: Optional[str] = Column(String, index=True, nullable=True)
    username: str = Column(String, unique=True, index=True, nullable=False)
    hashed_password: str = Column(String, unique=True, index=True, nullable=False)
    lockers_counter: int = Column(Integer, index=True, nullable=False, default=0)
    personal_user_salt: str = Column(String, index=True, nullable=True)

    lockers = relationship(Locker, back_populates="owner")

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def get_name(self):
        if self.name is not None:
            return self.name
        else:
            return None

    def get_surname(self):
        if self.surname is not None:
            return self.surname
        else:
            return None

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def to_dict(self):
        return {
            "uuid": str(self.uuid),
            "name": self.name,
            "surname": self.surname,
            "username": self.username,
            "password": self.password
        }
