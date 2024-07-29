import random

from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.LockBoxDBManager import BaseModel


class User(BaseModel):

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    uuid = uuid4()
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, nullable=True)
    surname = Column(String, index=True, nullable=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, unique=True, index=True, nullable=False)
    lockers_counter = Column(Integer, index=True, nullable=False, default=0)
    personal_user_salt = Column(String, index=True, nullable=True)

    lockers = relationship("Locker", back_populates="owner")


class Locker(BaseModel):

    __tablename__ = "lockers"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    service_name = Column(String, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, unique=True, index=True, nullable=False)
    locker_owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="lockers")

    bg_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
