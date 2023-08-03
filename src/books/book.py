from abc import ABC, abstractmethod

from src.helpers.logger_helper import LoggerHelper
from src.helpers.singleton_helper import SingletonHelper


class Book(ABC):
    def __init__(self, singleton_provider: SingletonHelper, config):
        self.__logger = singleton_provider.get_singleton(LoggerHelper) if singleton_provider.has_singleton(LoggerHelper) else None
        self._config = config


    def get_all_sport_data(self) -> list:
        matchs= []
        if self.__logger != None:
            self.__logger.info(f"{self._config['name']}: Fetching...")
        for book_config in self._config["bookConfig"]:
            match = self.get_sport_data(book_config)
            if self.__logger != None:
                self.__logger.debug(f"Fetching {self._config['name']} {book_config['sport']}.")
            if match != None:
                matchs.extend(match)
        if self.__logger != None:
            self.__logger.info(f"{self._config['name']}: Found {len(matchs)} events.")
        return matchs


    @abstractmethod
    def get_sport_data(self, book_config):
        pass
