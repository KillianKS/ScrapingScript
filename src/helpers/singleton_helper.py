from typing import TypeVar


class SingletonHelper():
    def __init__(self):
        self.__singleton = {}


    T = TypeVar("T")
    def get_singleton(self, class_type: T) -> T:
        class_name = class_type.__name__
        instance = self.__singleton.get(class_name)
        if instance == None:
            raise f"No instance for {class_type.__name__}"
        return instance


    def has_singleton(self, *class_types):
        for class_type in class_types:
            if self.__singleton.get(class_type.__name__) == None:
                return False
        return True


    def has_singleton_or_exeption(self, *class_types):
        if not self.has_singleton(*class_types):
            raise f"No singleton hase been found: {class_types}"


    def add_singleton(self, class_type, *args):
        self.add_singleton_interface(class_type, class_type, *args)


    def add_singleton_interface(self, class_type_interface, class_type, *args):
        class_name = class_type_interface.__name__
        instance = self.__singleton.get(class_name)
        if instance == None:
            self.__singleton[class_name] = class_type(*args)


    def delete_singleton(self, class_type):
        class_name = class_type.__name__
        instance = self.__singleton.get(class_name)
        if instance != None:
            self.__singleton.pop(class_name)
