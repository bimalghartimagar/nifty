from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from dao.base import Base

class Banks(Base):
    __tablename__ =  'banks'
    id = Column(Integer, primary_key=True)
    bank_name = Column(String(250), nullable=False)
    bank_symbol = Column(String(10), unique=True, nullable=False)
    # forex = relationship('Forex')

    def __init__(self, bank_name, bank_symbol):
        self.bank_name = bank_name
        self.bank_symbol = bank_symbol