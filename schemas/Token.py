from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    expiring_time: float


class TokenData(BaseModel):
    username: str or None = None
