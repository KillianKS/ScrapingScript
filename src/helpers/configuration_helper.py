from dotenv import dotenv_values


class ConfigurationHelper():
    def __init__(self):
        self.__configs: dict[str, object] = dotenv_values(".env")


    def addConfig(self, key: str, value: object):
        self.__configs[key] = value


    def concate(self, configs: dict[str, object]):
        self.__configs = self.__configs | configs


    def getConfig(self, key: str):
        return self.__configs.get(key)
