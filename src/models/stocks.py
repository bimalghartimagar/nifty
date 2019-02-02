""" Stocks Model """

from sqlalchemy import Column, Integer, String, Date, Float

from src.dao.base import Base


class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(20), nullable=False)
    name = Column(String(250), nullable=False)
    trade_date = Column(Date, nullable=False)
    trade_value = Column(Float, nullable=False)

    def __init__(self, symbol, name, trade_date, trade_value):
        self.symbol = symbol
        self.name = name
        self.trade_name = trade_name
        self.trade_value = trade_value
