# from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date, Float
# from sqlalchemy.orm import sessionmaker, Session, relationship
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.dialects.postgresql import insert
# from datetime import datetime

# def _create_session():
#     DeclBase = declarative_base()

#     class Users(DeclBase):
#         __tablename__ = 'users'
#         id = Column(Integer, primary_key=True)
#         name = Column(String(250), nullable=False)

#         def __init__(self, name):
#             self.name = name

#     class Banks(DeclBase):
#         __tablename__ =  'banks'
#         id = Column(Integer, primary_key=True)
#         bank_name = Column(String(250), nullable=False)
#         bank_symbol = Column(String(10), unique=True, nullable=False)
#         forex = relationship('Forex')

#         def __init__(self, bank_name, bank_symbol):
#             self.bank_name = bank_name
#             self.bank_symbol = bank_symbol

#     class Stock(DeclBase):
#         __tablename__ = 'stocks'
#         id = Column(Integer, primary_key=True)
#         symbol = Column(String(20), nullable=False)
#         name = Column(String(250), nullable=False)
#         trade_date = Column(Date, nullable=False)
#         trade_value = Column(Float, nullable=False)

#         def __init__(self, symbol, name, trade_date, trade_value):
#             self.symbol = symbol
#             self.name = name
#             self.trade_name = trade_name
#             self.trade_value = trade_value

#     class Forex(DeclBase):
#         __tablename__ = 'forex'
#         id = Column(Integer, primary_key=True)
#         currency = Column(String(5), nullable=False)
#         rate = Column(Float, nullable=False)
#         bank_id = Column(Integer, ForeignKey('banks.id'))
#         bank = relationship("Banks", backref="forex")

#         def __init__(self, currency, rate, bank):
#             self.currency = currency
#             self.rate = rate
#             self.bank = bank

#     engine = create_engine('postgresql://postgres:nepal123@localhost:5432/postgres')

#     DeclBase.metadata.create_all(engine)

#     Base = automap_base(DeclBase) 

#     Base.prepare(engine, reflect=True)

#     Customers = Base.classes.customers
#     States = Base.classes.states
#     Addresses = Base.classes.addresses
#     Orders = Base.classes.orders

#     session = Session(bind=engine)

#     states_data = [ 
#         { 'name':'Province No. 1', 'abbreviation':'PI' },
#         { 'name':'Province No. 2', 'abbreviation':'PT' },
#         { 'name':'Province No. 3', 'abbreviation':'PH' },
#         { 'name':'Gandaki', 'abbreviation':'GD' },
#         { 'name':'Province No. 5', 'abbreviation':'PF' },
#         { 'name':'Karnali', 'abbreviation':'KN' },
#         { 'name':'Sudurpashchim', 'abbreviation':'SP' }
#     ]

#     banks_data = [
#         {'bank_name': 'Nepal Rastra Bank', 'bank_symbol':'NRB'},
#         {'bank_name': 'Nepal Investment Bank Limited', 'bank_symbol':'NIBL'}
#     ]
#     # Load states data
#     statement = insert(States).values(states_data).on_conflict_do_nothing(index_elements=['abbreviation'])
#     session.execute(statement)

#     # Load banks data
#     statement = insert(Banks).values(banks_data).on_conflict_do_nothing(index_elements=['bank_symbol'])
#     session.execute(statement)
#     session.commit()

#     return session

# session = _create_session()

# def add_forex(forex_list):
#     for currency, rate in banks:
#         session.Add(Forex(currency, rate))
#     return session.commit()

# # states = session.query(States)
# # print(states.all())

# # banks = session.query(Banks)
# # print(banks.all())
