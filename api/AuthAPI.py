from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.hash import pbkdf2_sha512
from sqlalchemy.orm import Session
from starlette import status

from database.LockBoxDBManager import SessionLocal
from dbcrud.users import UserController
from schemas.UserBase import UserBase, UserCreate, User
from schemas.Token import Token, TokenData

SECRET_KEY = "5178e2f29aeb14025f3463c981240c074a77464b0572992e3f3b5a7491c694a3"
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
AuthAPI = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_password(plain, hashed):
    return pbkdf2_sha512.verify(plain, hashed)


def get_password_hash(password):
    return pbkdf2_sha512.hash(password)


def auth_user(db_session: Session, username: str, password: str):
    req_user = UserController.get_user_by_username(db_session, username=username)
    if not req_user:
        print("[LOG]: No user found with given username")
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(password, req_user.hashed_password):
        print("[LOG]: Incorrect password")
        raise HTTPException(status_code=400, detail="Incorrect password")
    return req_user


def create_access_token(data: dict, expiring_time: timedelta or None = None):
    to_encode = data.copy()
    expire = datetime.now() + (expiring_time or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db_session: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            print("[LOG]: No user found with given username")
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        print("[LOG]: JWTError (Could not validate token)")
        raise credentials_exception

    user = UserController.get_user_by_username(db_session, username=token_data.username)
    if user is None:
        print("[LOG]: No user found with given username")
        raise credentials_exception

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user:
        print("[LOG]: No user")
        raise HTTPException(status_code=400, detail="No user")
    return current_user


@AuthAPI.get("/users/me/", response_model=User)
def read_user(current_user: User = Depends(get_current_active_user)):
    return current_user


@AuthAPI.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_user(db, form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expiring_time=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@AuthAPI.post("/register/", response_model=UserBase)
async def register(user: UserCreate, db_session: Session = Depends(get_db)):
    existing_user = UserController.get_user_by_username(db_session, username=user.username)
    if existing_user:
        print("[LOG]: Username already registered")
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    return UserController.create_user(db=db_session, user=user, salt=user.personal_user_salt)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(AuthAPI, host="0.0.0.0", port=8080)
