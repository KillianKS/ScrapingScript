from time import sleep
import argparse

from src.database.database import Database
from src.database.local_database import LocalDatabase
from src.database.mango_database import MangoDatabase
from src.services.books_retrieve_service import BooksRetrieveService
from src.services.notify_events_sender_service import NotifyEventsSenderService
from src.helpers.configuration_helper import ConfigurationHelper
from src.helpers.singleton_helper import SingletonHelper
from src.helpers.logger_helper import LoggerHelper


def init_books_retrieve_singleton(args) -> SingletonHelper:
    singleton_provider = SingletonHelper()
    singleton_provider.add_singleton(LoggerHelper, "books_retrieve", args.verbose)
    singleton_provider.add_singleton(ConfigurationHelper)
    singleton_provider.add_singleton_interface(Database, LocalDatabase, singleton_provider)
    return singleton_provider


def init_notify_events_sender_singleton(args) -> SingletonHelper:
    singleton_provider = SingletonHelper()
    singleton_provider.add_singleton(LoggerHelper, "notify_events_sender", args.verbose)
    singleton_provider.add_singleton(ConfigurationHelper)
    singleton_provider.add_singleton_interface(Database, LocalDatabase, singleton_provider)
    return singleton_provider


def main(args):
    books_retrieve_singleton = init_books_retrieve_singleton(args)
    books_retrieve = BooksRetrieveService(books_retrieve_singleton)

    notify_events_sender_singleton = init_notify_events_sender_singleton(args)
    notify_events_sender = NotifyEventsSenderService(notify_events_sender_singleton)

    while True:
        try:
            books_retrieve.init_books(not args.noproxy)
            books_retrieve.retrieve_all_books_multi_thread(3)
        except Exception as ex:
            books_retrieve_singleton.get_singleton(LoggerHelper).exception(ex)

        try:
            notify_events_sender.send_not_notify_bets()
        except Exception as ex:
            notify_events_sender_singleton.get_singleton(LoggerHelper).exception(ex)

        sleep(120)


def _args_parser():
    parser = argparse.ArgumentParser(
        description="OddOpening, odd scrapper and notification"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="Increases logging",
        default=True
    )
    parser.add_argument(
        "-np",
        "--noproxy",
        dest="noproxy",
        action="store_true",
        help="Disable Proxy's",
        default=True
    )

    return parser.parse_args()


if __name__ == '__main__':
    main(_args_parser())
