from multiprocessing.pool import ThreadPool
from src.books import BOOKS_CLASS
from src.books.book import Book
from src.database.database import Database
from src.tools.array_tools import find
from src.tools.exception_tools import safe_call
from src.helpers.configuration_helper import ConfigurationHelper
from src.helpers.singleton_helper import SingletonHelper
from src.helpers.logger_helper import LoggerHelper
from src.helpers.http_helper import HTTPHelper


class BooksRetrieveService():
    def __init__(self, singleton_provider: SingletonHelper):
        singleton_provider.has_singleton_or_exeption(ConfigurationHelper, Database, LoggerHelper)

        self.__database = singleton_provider.get_singleton(Database)
        self.__logger = singleton_provider.get_singleton(LoggerHelper)
        self.__singleton_provider = singleton_provider

        self.__books: list[Book] = []


    def init_books(self, http_use_proxy=None):
        self.__books = []
        self.__singleton_provider.delete_singleton(HTTPHelper)
        if http_use_proxy != None:
            self.__singleton_provider.add_singleton(HTTPHelper, http_use_proxy)
        else:
            self.__singleton_provider.add_singleton(HTTPHelper)
        for config in self.__database.get_actives_books_config():
            book = find(BOOKS_CLASS, lambda book_class: book_class.__name__ == config['name'])
            if book != None:
                # TODO? create a new instance for each book ?
                self.__books.append(book(self.__singleton_provider, config))
                self.__logger.info("Book '%s' init", config['name'])
            else:
                self.__logger.warning("Book '%s' have no class", config['name'])


    def retrieve_all_books_multi_thread(self, thread_process=10):
        with ThreadPool(thread_process) as pool:
            async_pool = pool.map_async(
                safe_call(self.__logger, lambda book: book.get_all_sport_data()),
                self.__books
            )

            try:
                for events in async_pool.get(timeout=10 * 60):
                    for event in events:
                        self.__database.upsert_event(event)
            except TimeoutError as ex:
                self.__logger.error(ex, stack_info=True, exc_info=True)
            except Exception as ex:
                self.__logger.error(ex, stack_info=True, exc_info=True)


    def retrieve_all_books(self):
        for book in self.__books:
            try:
                self.__retrieve_book(book)
            except Exception as ex:
                self.__logger.error(ex, stack_info=True, exc_info=True)


    def retrieve_book(self, bookName: str):
        book = find(self.__books, lambda book: book.config.get("name") == bookName)
        if book == None:
            raise f"Unknown book {bookName}. Know books: {[book._config.get('name') for book in self.__books]}"
        self.__retrieve_book(book)


    def __retrieve_book(self, book: Book):
        data = book.get_all_sport_data()
        for match in data:
            self.__database.upsert_bet(match)
