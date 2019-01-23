from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from dao.base import Base

class Forex(Base):
    __tablename__ = 'forex'
    id = Column(Integer, primary_key=True)
    currency = Column(String(5), nullable=False)
    rate = Column(Float, nullable=False)
    bank_id = Column(Integer, ForeignKey('banks.id'))
    bank = relationship("Banks", backref="forex")

    def __init__(self, currency, rate, bank):
        self.currency = currency
        self.rate = rate
        self.bank = bank