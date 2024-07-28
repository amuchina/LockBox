import random

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import models
from LockBoxDBManager import BaseModel


def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


class Locker(BaseModel):

    __tablename__ = "lockers"

    id = Column(Integer, primary_key=True)
    service_name = Column(String, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, unique=True, index=True, nullable=False)
    locker_owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship(models.User, back_populates="lockers")

    bg_color = generate_random_color()

    def save(self, hashencrypter, salt):
        encrypted_password_data = hashencrypter.gen_sha256_digest(salt=salt, password=self.password)  # this only goes to db, it is not the encrypted password
        print(encrypted_password_data)

    def to_string(self):
        return f"Locker(service_name='{self.service_name}', username='{self.username}', password='{self.password}')"

    def to_list(self):
        return [self.service_name, self.username, self.password, self.lockers_owner_id]

