# server
from flask import Flask
from .db.database import Session, engine, Base
from .db import model

Base.matadata.create_all(engine)


def get_db():
    database = Session()
    try:
        yield database
    finally:
        database.close()
