import requests


class WebhookHelper():
    def __init__(self, url: str):
        self.__url = url


    def send(self, json):
        return requests.post(self.__url, json=json).content
