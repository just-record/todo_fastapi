from sqlalchemy.orm import Session
from models.models import User
from passlib.context import CryptContext 


def hash_password(password: str):
    bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
    return bcrypt_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
    return bcrypt_context.verify(plain_password, hashed_password)


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_name(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: User):
    user.password = hash_password(user.password)
    db_user = User(**dict(user))
    db.add(db_user)
    db.commit() 
    db.refresh(db_user)
    return db_user