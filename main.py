from fastapi import FastAPI
from db.database import engine
from models.models import Base

from api.endpoints import users
from api.endpoints import auth
from api.endpoints import todos

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)

@app.get("/")

def read_root():
    return {"message": "Hello, FastAPI!"}