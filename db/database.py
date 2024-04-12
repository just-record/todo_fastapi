from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import Config

config = Config().get_config()

db_host = config['database']['db_host']
db_port = config['database']['db_port']
db_name = config['database']['db_name']
db_user = config['database']['db_user']
db_password = config['database']['db_password']


SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, future=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
Base = declarative_base()