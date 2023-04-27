from sqlalchemy import create_engine,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv.main import load_dotenv
import os


load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_LINK']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




#database connection establishment
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()