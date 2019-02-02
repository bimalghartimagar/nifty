from dao.base import Session
from models.banks import Banks
from models.forex import Forex

session = Session()

def add_forex(forex_list):
    for currency, rate in banks:
        session.Add(Forex(currency, rate))
    return session.commit()

def get_bank_list():
    return session.query(Banks).all()