from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('postgresql://<USERNAME>:<PASSWORD>@<HOSTNAME>:<PORT>/<DB_NAME>')

Base.metadata.create_all(engine)

session = Session(bind=engine)