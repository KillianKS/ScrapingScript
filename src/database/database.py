from abc import ABC, abstractclassmethod

from src.helpers.singleton_helper import SingletonHelper


class Database(ABC):
    @abstractclassmethod
    def __init__(singleton_provider: SingletonHelper):
        pass


    @abstractclassmethod
    def upsert_event(self, event):
        pass


    @abstractclassmethod
    def event_is_notify(self, eventId):
        pass


    @abstractclassmethod
    def get_actives_books_config(self):
        pass


    @abstractclassmethod
    def get_not_notify_events(self):
        pass