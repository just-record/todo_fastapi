from sqlalchemy.orm import Session
from models.models import User
from passlib.context import CryptContext
import logging


logger = logging.getLogger(__name__)


def hash_password(password: str):
    bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
    return bcrypt_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
    return bcrypt_context.verify(plain_password, hashed_password)


def get_user(db: Session, user_id: int):
    try:
        return db.query(User).filter(User.id == user_id).first()
    except Exception as e:
        logger.error(f'Error: {e}')
        raise e


def get_user_by_name(db: Session, username: str):
    try:
        return db.query(User).filter(User.username == username).first()
    except Exception as e:
        logger.error(f'Error: {e}')
        raise e


def create_user(db: Session, user: User):
    try:
        user.password = hash_password(user.password)
        db_user = User(**dict(user))
        db.add(db_user)
        db.commit() 
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        logger.error(f'Error: {e}')
        raise e