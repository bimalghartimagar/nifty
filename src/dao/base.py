from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from utils.config import get_config

DATABASE_URI = get_config().DATABASE_URI

Base = declarative_base()

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)

session = Session(bind=engine)