from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://user01:user01password@localhost/db01"
SQLALCHEMY_DATABASE_URL = "postgresql://user01:user01@localhost/mydatabase"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, future=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
Base = declarative_base()