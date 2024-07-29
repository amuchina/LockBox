import mysql.connector
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

load_dotenv("../env/.env.secret.db")


class Base:
    __allow_unmapped__ = True


BaseModel = declarative_base(cls=Base)

try:
    dbengine = create_engine("mysql://root:password@localhost/lockbox")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=dbengine)
    print("Successfully connected to database")
except exc.SQLAlchemyError as err:
    raise mysql.connector.Error(f"Connection is not established or has been closed ({err})")
