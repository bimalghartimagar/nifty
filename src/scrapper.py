from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests

from src.utils import utility

class Scrapper(ABC):

    @abstractmethod
    def scrape_data(self):
        pass

scrappers = { }

class NIBLScrapper(Scrapper):

    def scrape_data(self):
        print('Scrapping NIBL data')
        r=requests.get('https://www.nibl.com.np/forex/', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        for a in b.find_all('tr')[2].find_all('td')[2].stripped_strings:
            rate = float(a) 
        print('Scrapping successful, NIBL rate is {}'.format(rate))
        return round(float(rate),2)
        
class NRBScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping NRB data')
        r=requests.get('https://www.nrb.org.np/fxmexchangerate.php', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[4].find_all('tr')[7].find_all('td')[2].find('font').string
        print('Scrapping successful, NRB rate is {}'.format(rate))
        return round(float(rate),2)

class NMBScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping NMB data')
        r=requests.get('http://nmbbanknepal.com/forex', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[2].find_all('td')[2].string
        print('Scrapping successful, NMB rate is {}'.format(rate))
        return round(float(rate),2)

class SBLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping SBL data')
        r=requests.get('https://www.sanimabank.com/forex', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('div', class_='forex-wrap')[1].find_all('div',class_='rate')[1].find('p').string
        print('Scrapping successful, SBL rate is {}'.format(rate))
        return round(float(rate),2)

class EBLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping EBL data')
        r=requests.get('https://www.everestbankltd.com/supports/interest-and-rates/forex/', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[11].find_all('td')[3].string
        print('Scrapping successful, EBL rate is {}'.format(rate))
        return round(float(rate),2)

class SBIScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping SBI data')
        r=requests.get('https://nepalsbi.com.np/content/foreign-exchange-rates.cfm', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[1].find_all('td')[3].string
        print('Scrapping successful, SBI rate is {}'.format(rate))
        return round(float(rate),2)

class NBLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping NBL data')
        r=requests.get('https://www.nepalbank.com.np/exchange-rate', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[1].find_all('tr')[1].find_all('td')[2].string
        print('Scrapping successful, NBL rate is {}'.format(rate))
        return round(float(rate),2)

class LBBLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping LBBL data')
        r=requests.get('http://www.lumbinibikasbank.com/site/get_updated_forex_rate', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[1].find_all('td')[3].string
        print('Scrapping successful, LBBL rate is {}'.format(rate))
        return round(float(rate),2)

class BOKLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping BOKL data')
        r=requests.get('https://www.bok.com.np/forex', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[1].find_all('td')[4].string
        print('Scrapping successful, BOKL rate is {}'.format(rate))
        return round(float(rate),2)

class NABILScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping NABIL data')
        r=requests.get('https://www.nabilbank.com/exchange-rate', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[2].find_all('td')[2].string
        rate = utility.clean_escaped_strings(rate)
        print('Scrapping successful, NABIL rate is {}'.format(rate))
        return round(float(rate),2)

class HBLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping HBL data')
        r=requests.get('https://himalayanbank.com/forex', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[1].find_all('td')[3].string
        print('Scrapping successful, HBL rate is {}'.format(rate))
        return round(float(rate),2)

class GIBScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping GIB data')
        r=requests.get('http://globalimebank.com/forex.html', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[2].find_all('tr')[2].find_all('td')[4].string
        print('Scrapping successful, GIB rate is {}'.format(rate))
        return round(float(rate),2)

class MBLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping MBL data')
        r=requests.get('https://www.machbank.com/forex', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[1].find_all('td')[3].string
        print('Scrapping successful, MBL rate is {}'.format(rate))
        return round(float(rate),2)

class ADBLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping ADBL data')
        r=requests.get('http://www.adbl.gov.np/adbl_exchange_rate.html', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[2].find_all('td')[4].string
        print('Scrapping successful, ADBL rate is {}'.format(rate))
        return round(float(rate),2)

class MBScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping MB data')
        r=requests.get('https://www.megabanknepal.com/page/exchange-rate', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[0].find_all('td')[2].string
        print('Scrapping successful, MB rate is {}'.format(rate))
        return round(float(rate),2)

class SCBLScrapper(Scrapper):
    
    def scrape_data(self):
        print('Scrapping SCBL data')
        r=requests.get('https://www.sc.com/np/bank-with-us/forex-solution/foreign-currency-exchange-rates/', timeout=10)
        b = BeautifulSoup(r.content, "html.parser")
        rate = b.find_all('table')[0].find_all('tr')[3].find_all('td')[3].string
        print('Scrapping successful, SCBL rate is {}'.format(rate))
        return round(float(rate),2)

scrappers = {
    'NIBL': NIBLScrapper(),
    'NRB': NRBScrapper(),
    'NMB': NMBScrapper(),
    'SBL': SBLScrapper(),
    'SCBL': SCBLScrapper(),
    'EBL': EBLScrapper(),
    'SBI': SBIScrapper(),
    'NBL': NBLScrapper(),
    'LBBL': LBBLScrapper(),
    'BOKL': BOKLScrapper(),
    'NABIL': NABILScrapper(),
    'HBL': HBLScrapper(),
    'GIB': GIBScrapper(),
    'MBL': MBLScrapper(),
    'ADBL': ADBLScrapper(),
    'MB': MBScrapper()
}

if __name__ == "__main__":
    LBBLScrapper().scrape_data()