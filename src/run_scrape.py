from threading import Thread

from src.abstract_scrape import ConcreteScrapperCreator
from src.worker import ScrapeWorker
from src.utils.utility import rate_sort

concrete_creator = ConcreteScrapperCreator()


def run(bank_symbol_list):
    rate_list = []
    worker_list = []

    for bank_symbol in bank_symbol_list:
        worker = ScrapeWorker(bank_symbol, rate_list)
        worker.start()
        worker_list.append(worker)

    for worker in worker_list:
        worker.join()

    print('Completed scrapping all sites')
    print(rate_list)
    rate_list.sort(key=rate_sort, reverse=True)
    return rate_list

def get_scraped_data(bank_symbol_list):
    rate_list = []
    for bank_symbol in bank_symbol_list:
        rate = concrete_creator.get_scrapper(bank_symbol).scrape_data()
        rate_list.append({'symbol': bank_symbol, 'rate': rate})
    print('Completed scrapping from request')
    return rate_list


if __name__ == "__main__":
    site_list = ['NIBL', 'NRB', 'NMB', 'SBL', 'SCBL', 'LBBL']
    rates = run(site_list)
    print(rates)