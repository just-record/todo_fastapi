from fastapi import FastAPI
from db.database import engine
from models.models import Base

from api.endpoints import users
from api.endpoints import auth
from api.endpoints import todos

from core.init_config import init

init()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)