from src.senders import SENDERS_CLASS
from src.senders.sender import Sender
from src.database.database import Database
from src.helpers.configuration_helper import ConfigurationHelper
from src.helpers.singleton_helper import SingletonHelper


class NotifyEventsSenderService():
    def __init__(self, singleton_provider: SingletonHelper):
        singleton_provider.has_singleton_or_exeption(ConfigurationHelper, Database)
        self.__database = singleton_provider.get_singleton(Database)

        self.__senders: list[Sender] = [sender_class(singleton_provider) for sender_class in SENDERS_CLASS]


    def send_not_notify_bets(self):
        bets = self.__database.get_not_notify_events()
        for bet in bets:
            self.__senders_send_bet(bet)


    def __senders_send_bet(self, bet):
        for sender in self.__senders:
            formated_match = sender.format_match(bet)
            sender.send(formated_match)