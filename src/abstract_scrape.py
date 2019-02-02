""" Factory Module for creating scrappers """

from abc import ABC, abstractmethod

from src.scrapper import *


class ScrapperCreator(ABC):
    """ Scrapper Factory """

    @abstractmethod
    def get_scrapper(self, scrapper_type):
        """ Factory method to return the concrete scapper object """
        pass


class ConcreteScrapperCreator(ScrapperCreator):
    """ Concrete factory creator for scrapper object """
    def __init__(self):
        self.scrappers = scrappers

    def get_scrapper(self, scrapper_type):

        return self.scrappers[scrapper_type]
