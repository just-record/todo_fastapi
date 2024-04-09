from fastapi import FastAPI
from db.database import SessionLocal, engine
from models.models import Base

from api.endpoints import users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

@app.get("/")

def read_root():
    return {"message": "Hello, FastAPI!"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()