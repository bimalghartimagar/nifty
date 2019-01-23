from sqlalchemy import Column, Integer, String

from dao.base import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, name):
        self.name = name