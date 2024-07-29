from pydantic import BaseModel


class LockerBase(BaseModel):
    service_name: str
    locker_owner_id: int


class LockerCreate(LockerBase):
    username: str
    password: str


class Locker(LockerBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
