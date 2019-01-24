from threading import Thread

from abstract_scrape import ConcreteScrapperCreator
concrete_creator = ConcreteScrapperCreator()


class ScrapeWorker(Thread):

    def __init__(self, bank_symbol, rates=[]):
        Thread.__init__(self)
        self.rates = rates
        self.bank_symbol = bank_symbol

    def run(self):
        rate = concrete_creator.get_scrapper(self.bank_symbol).scrape_data()

        self.rates.append({'symbol': self.bank_symbol, 'rate': rate})
