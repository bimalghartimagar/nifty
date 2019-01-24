from sqlalchemy.dialects.postgresql import insert

from models.banks import Banks
from dao.base import session

def run_initial():
    banks_data = [
        {'bank_name': 'Nepal Rastra Bank', 'bank_symbol':'NRB'},
        {'bank_name': 'Nepal Investment Bank Limited', 'bank_symbol':'NIBL'},
        {'bank_name': 'NMB Bank', 'bank_symbol':'NMB'},
        {'bank_name': 'Standard Chartered Bank', 'bank_symbol':'SCBL'},
        {'bank_name': 'Sanima Bank Limited', 'bank_symbol':'SBL'},
        {'bank_name': 'Everest Bank Limited', 'bank_symbol':'EBL'},
        {'bank_name': 'Nepal Sbi Bank Limited', 'bank_symbol':'SBI'},
        {'bank_name': 'Nepal Bank Limited', 'bank_symbol':'NBL'},
        {'bank_name': 'Lumbini Bikas Bank Ltd.', 'bank_symbol':'LBBL'},
        {'bank_name': 'Bank of Kathmandu Limited', 'bank_symbol':'BOKL'},
        {'bank_name': 'Nabil Bank', 'bank_symbol':'NABIL'},
        {'bank_name': 'Himalayan Bank Ltd.', 'bank_symbol':'HBL'},
        {'bank_name': 'Global IME Bank Ltd.', 'bank_symbol':'GIB'},
        {'bank_name': 'Machhapuchchhre Bank Limited', 'bank_symbol':'MBL'},
        {'bank_name': 'Agricultural Development Bank Limited', 'bank_symbol':'ADBL'},
        {'bank_name': 'Mega Bank Nepal Limited', 'bank_symbol':'MB'}
    ]

    # Load banks data
    statement = insert(Banks).values(banks_data).on_conflict_do_nothing(index_elements=['bank_symbol'])
    session.execute(statement)
    session.commit()

if __name__ == "__main__":
    run_initial()