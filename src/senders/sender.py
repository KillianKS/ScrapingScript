from abc import ABC, abstractclassmethod


class Sender(ABC):
    @abstractclassmethod
    def send(self, obj):
        pass # Check if succes and return in case of an error

    @abstractclassmethod
    def format_match(self, match):
        pass
