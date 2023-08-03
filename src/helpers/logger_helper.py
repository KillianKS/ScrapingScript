from __future__ import annotations
from os import makedirs, path
from datetime import datetime
import logging
import re


class LoggerHelper(logging.Logger):
    __DEFAULT_LOG_PATH = "./logs/{logger_name}_{timestamp}.log"


    def __init_handler_file_out(self, file_prefix: str):
        logger_name = re.sub("-+", "-", re.sub("[^A-Za-z0-9]", "-", file_prefix.lower()))
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = LoggerHelper.__DEFAULT_LOG_PATH.format(logger_name=logger_name,timestamp=timestamp)

        makedirs(path.dirname(filename), exist_ok=True)

        return logging.FileHandler(filename=filename, encoding='utf-8', mode='a')


    def __init__(self, log_prefix: str, verbose=False) -> None:
        super().__init__(log_prefix, logging.DEBUG if verbose else logging.INFO)

        self.__file_handler = self.__init_handler_file_out(log_prefix)
        for handler in [self.__file_handler, logging.StreamHandler()]:
            handler.setFormatter(logging.Formatter('[%(asctime)s:%(levelname)s] [%(filename)s:%(funcName)s] %(message)s', "%d-%m-%Y %H:%M:%S"))
            self.addHandler(handler)

        self.debug("Logger Init")


    def __del__(self):
        super().__del__()
        for handle in self.handlers:
            handle.flush()
            handle.close()
