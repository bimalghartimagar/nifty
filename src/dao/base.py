""" Base module for sqlalchemy database connection """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.utils.config import get_config

DATABASE_URL = get_config().DATABASE_URL

Base = declarative_base()

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
