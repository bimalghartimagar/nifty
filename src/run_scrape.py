from abstract_scrape import ConcreteScrapperCreator
from threading import Thread
concrete_creator = ConcreteScrapperCreator()

def run():
    site_list = ['NIBL', 'NRB']
    threads_list = []
    for site in site_list:
        t = Thread(target=concrete_creator.get_scrapper(site).scrape_data,
                    name=site,
                    args=())
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()
    
    print('Completed scrapping all sites')

def get_scraped_data(bank_symbol_list):
    rate_list = []
    for bank_symbol in bank_symbol_list:
        rate = concrete_creator.get_scrapper(bank_symbol).scrape_data()
        rate_list.append({'symbol':bank_symbol, 'rate': rate})
    print('Completed scrapping from request')
    return rate_list


