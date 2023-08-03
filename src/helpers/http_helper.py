import json
import random
import cloudscraper
from bs4 import BeautifulSoup


class HTTPHelper():
    # TODO: add logs
    def __init__(self, use_proxy=False):
        with open('residentials.txt', 'r') as f:
            self.__proxies = f.read().splitlines()
        with open('user-agents.txt', 'r') as f:
            self.__agent = f.read().splitlines()
        self.__use_proxy = use_proxy


    # create a new http session for each call
    def get(self, url, headers=None):
        session = cloudscraper.create_scraper()

        req_parameters = {}

        #region headers
        req_parameters["headers"] = {
            'User-Agent': random.choice(self.__agent)
        }
        if headers != None:
            req_parameters["headers"] = {**req_parameters["headers"], **headers}
        #endregion

        attempt = 0
        while attempt < 11:
            resp = None
            try:
                if self.__use_proxy:
                    req_parameters["proxys"] = {"https": f"http://{random.choice(self.__proxies)}"}
                resp = session.get(url, **req_parameters)
                pass
            except Exception as e:
                # logger.info(e)
                attempt += 1
                # logger.info("Attempt n°"+attempt)
            else:
                # logger.info("Download returned : 200")
                return resp
        return None


    def get_html(self, url, **parameters):
        content = self.get(url, **parameters).content
        return BeautifulSoup(content, 'html.parser')


    def get_json(self, url, **parameters):
        content = self.get(url, **parameters).content
        return json.loads(content)
