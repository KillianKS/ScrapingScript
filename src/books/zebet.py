from bs4 import BeautifulSoup

from src.books.book import Book
from src.helpers.singleton_helper import SingletonHelper
from src.helpers.http_helper import HTTPHelper
from src.helpers.logger_helper import LoggerHelper


class Zebet(Book):
    DEFAULT_URL = "https://www.zebet.fr"


    def __init__(self, singleton_provider: SingletonHelper, config):
        super().__init__(singleton_provider, config)
        singleton_provider.has_singleton_or_exeption(HTTPHelper, LoggerHelper)

        self.http_service = singleton_provider.get_singleton(HTTPHelper)
        self.logger = singleton_provider.get_singleton(LoggerHelper)


    def get_sport_data(self, book_config):
        url = self._config["url"].format(id=book_config["id"])
        self.logger.debug("get_sport_data url: %s", url)
        html = self.http_service.get_html(url)
        return self.get_page_data(html, book_config)


    def get_page_data(self, html, book_config):
        urls = self.get_sport_url_events(html)
        len(urls) > 0 and self.logger.debug("parsing folowing urls: %s", ','.join(urls))
        events = []
        for url in urls:
            self.logger.debug("[START]\tparsing event from url: %s", url)
            event = self.get_event(url, book_config)
            self.logger.debug("[END]\tparsing event from url: %s", url)
            events.append(event)
        return events


    def get_sport_url_events(self, html):
        sport_section = html.find(id="sport-all")
        try:
            return [Zebet.DEFAULT_URL + node_a["href"] for node_a in sport_section.find_all("a", href=True)]
        except:
            self.logger.warning("page not found")
            return []


    def get_event(self, url: str, book_config):
        html = self.http_service.get_html(url)

        node_content = html.find(id="content")
        node_title_green = node_content.find_all(class_="title-green", limit=2)[1]
        event_name = node_title_green.find_next("span").getText().strip().replace("1\u00e8re", "1ere")

        return {
            "event": book_config["id"],
            "name": event_name,
            "bookmaker": self._config["name"],
            "sport": book_config["sport"],
            "allBet4match": self.get_sub_event(url),
            "url": url,
            "notify": None,
            "expireAt": None
        }


    def get_sub_event(self, url: str):
        html = self.http_service.get_html(url)
        nodes_bet = self.get_sub_event_bets(html)
        allBet4match = []
        for node in nodes_bet:
            if "grouped_questions" in node["class"]:
                allBet4match.extend(self.parse_page_tab_bets(node))
            elif node.find(class_="bet-activebets") is not None:
                allBet4match.append(self.parse_page_sub_bets(node))
            else:
                allBet4match.append(self.parse_page_all_bets(node))
        return allBet4match


    def get_sub_event_bets(self, html: BeautifulSoup):
        nodes_class_accordion_wrapper = html.select("div.uk-accordion-wrapper.item-bloc.item")
        nodes_bet = []
        for node in nodes_class_accordion_wrapper:
            nodes_accordion_content = node.find(class_="uk-accordion-content")
            nodes_child_div = nodes_accordion_content.find_all("div", recursive=False)

            if len(nodes_child_div) == 1 and "class" not in nodes_child_div[0].attrs:
                nodes_bet.extend(nodes_child_div[0].find_all("div", recursive=False))
            else:
                nodes_bet.extend(nodes_child_div)
        return nodes_bet


    def parse_page_all_bets(self, node: BeautifulSoup):
        node_class_bet_name = node.find_next(class_="bet-question")
        betName = None

        if node_class_bet_name is not None:
            betName = node_class_bet_name.getText().strip()
        else:
            node_class_bet_name = node.find_next(class_="bet-time")
            if node_class_bet_name is not None:
                betName = node_class_bet_name.getText().strip()

        betId = node.find(attrs={"data-hash": True}).attrs.get("data-hash", None)
        if betId is not None:
            betId = betId[:8]

        nodes_actor = node.find_all(class_="pmq-cote-acteur")
        nodes_bet = node.find_all(class_="pmq-cote")
        cotes = []
        for entry in zip(nodes_actor, nodes_bet):
            actor = entry[0].getText().strip()
            odd = entry[1].getText().strip().replace("\u202f", " ")
            cotes.append({ "player": actor, "cote": odd})
        return {"name": betName, "betId": betId, "odd": cotes}


    def parse_page_sub_bets(self, node: BeautifulSoup):
        nodes_class_bet_activebets = node.find_next(class_="bet-activebets")
        nodes_a = nodes_class_bet_activebets.find_all("a", href=True)
        urls = [Zebet.DEFAULT_URL + node["href"] for node in nodes_a]
        allBet4match = []
        for url in urls:
            allBet4match.extend(self.get_sub_event(url))
        return allBet4match


    def parse_page_tab_bets(self, node: BeautifulSoup):
        node_tab_rows = node.find_all(class_="uk-flex uk-flex-middle uk-flex-space-between uk-flex-wrap uk-grid-small")
        node_tab_headers = node_tab_rows.pop(0).findChildren("span")

        bet_names = [node_tab_header.getText().strip() for node_tab_header in node_tab_headers]
        nodes_actors = [node_tab_row.find(class_="pmq-cote-acteur") for node_tab_row in node_tab_rows]
        actor_names =  [node_actor.getText().strip() for node_actor in nodes_actors]
        nodes_bets = [node_tab_row.findChildren(class_="pmq-cote") for node_tab_row in node_tab_rows]
        odd_values =  [[bet.getText().strip() for bet in nodes_bet] for nodes_bet in nodes_bets]

        betId = node.find(attrs={"data-hash": True}).attrs.get("data-hash", None)
        if betId is not None:
            betId = betId[:8]

        events = []
        for i in range(len(bet_names)):
            cotes = [{"player": entry[0], "cote": entry[1][i]} for entry in zip(actor_names, odd_values)]
            events.append({"name": bet_names[i], "betId": betId, "odd": cotes})
        return events
