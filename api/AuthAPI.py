from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

AuthAPI = FastAPI()


class (BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


tasks = []


@AuthAPI.get("/")
def read():
    return {}


@AuthAPI.post("/post/", response_model=Task)
def post(num):
    return num


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(AuthAPI, port=8080)
