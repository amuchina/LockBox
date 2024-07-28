from fastapi import FastAPI, HTTPException
from models.User import User
from Authenticator import Authenticator
import LockBoxDBManager as dbm

lockboxdbcontroller = dbm.connect()
AuthAPI = FastAPI()

authenticator = Authenticator()

tasks = []


@AuthAPI.post("/login")
def read():
    return {}


@AuthAPI.post("/register", response_model=User)
def register(user: User):
    if authenticator.register(newuser=user, dbcontroller=lockboxdbcontroller):
        return "Successfully signed up new user: " + user.to_dict()
    elif authenticator.register(newuser=user, dbcontroller=lockboxdbcontroller) == "NL":
        raise HTTPException(status_code=400, detail="Not logged in (Authenticator error)")
    elif authenticator.register(newuser=user, dbcontroller=lockboxdbcontroller) == "IE":
        raise HTTPException(status_code=400, detail="User already exists (DB error)")
    elif authenticator.register(newuser=user, dbcontroller=lockboxdbcontroller) == "GE":
        raise HTTPException(status_code=400, detail="Generic DB error")
    else:
        raise HTTPException(status_code=400, detail="Unknown error")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(AuthAPI, port=8080)
