from sqlalchemy.orm import Session
from models.models import User

def verify_password(plain_password: str, hashed_password: str):
    return plain_password == hashed_password


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_name(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: User):
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit() 
    db.refresh(db_user)
    return db_user