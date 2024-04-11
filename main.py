from fastapi import FastAPI
from db.database import SessionLocal, engine
from models.models import Base

from api.endpoints import users
from api.endpoints import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")

def read_root():
    return {"message": "Hello, FastAPI!"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()