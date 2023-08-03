import re
from datetime import datetime

from src.books.book import Book
from src.helpers.singleton_helper import SingletonHelper
from src.helpers.http_helper import HTTPHelper


class Parionssport(Book):
    URL_TOKEN = "https://www.enligne.parionssport.fdj.fr/lvs-api/acc/token"
    URL_BET = "https://www.enligne.parionssport.fdj.fr/lvs-api/next/50/p{}"
    URL_PAGE_BET = "https://www.enligne.parionssport.fdj.fr/paris-{}/{}/{}/{}/{}"

    def __init__(self, singleton_provider: SingletonHelper, config):
        super().__init__(singleton_provider, config)
        singleton_provider.has_singleton_or_exeption(HTTPHelper)

        self.http_service = singleton_provider.get_singleton(HTTPHelper)
        self.token = self.get_token()


    def get_token(self):
        return self.http_service.get_json(Parionssport.URL_TOKEN)["hsToken"]


    def get_sport_data(self, sport_config):
        data = self.http_service.get_json(
            self._config.get("url").format(id=sport_config.get("id")),
            headers={"X-LVS-HSToken": self.token}
        ).get("items")

        bets_raw = [{"id": key, **value} for key, value in data.items() if key[0] == "e"]
        matchs_raw = [{"id": key, **value} for key, value in data.items() if key[0] == "m"]
        odds_raw = [{"id": key, **value} for key, value in data.items() if key[0] == "o"]

        return [self.parse_bet(bet_raw, matchs_raw, odds_raw) for bet_raw in bets_raw]


    def parse_bet(self, bet, matchs_raw, odds_raw):
        eventId = bet.get("id")[1:]
        name = "{} {} - {}".format(bet.get("path").get("Category"), bet.get("path").get("League"), bet.get("desc"))
        time = datetime.strptime(bet.get("start"), '%y%m%d%H%M').isoformat()
        url = Parionssport.URL_PAGE_BET.format(
            self.str_to_url(bet.get("path").get("Sport")),
            self.str_to_url(bet.get("path").get("Category")),
            self.str_to_url(bet.get("path").get("League")),
            eventId,
            self.str_to_url(bet.get("desc"))
        )

        bet_matchs_raw = [match for match in matchs_raw if match.get("parent") == bet.get("id")]
        allBet4match = [
            self.parse_bet_odd(match_raw, [
                odd_raw
            for odd_raw in odds_raw if odd_raw.get("parent") == match_raw.get("id")])
        for match_raw in bet_matchs_raw]

        return {
            "event": eventId,
            "name": name,
            "bookmaker": "ParionsSport",
            "sport": bet.get("path").get("Sport"),
            "allBet4match": allBet4match,
            "url": url,
            "notify": None,
            "expireAt": time
        }


    def str_to_url(self, str):
        parse_str = re.sub("[^A-Za-z0-9]", "-", str.lower())
        return re.sub("-+", "-", parse_str)


    def parse_bet_odd(self, match_raw, odds_raw):
        odd = [{
            "player": odd_raw.get("desc"),
            "cote": float(odd_raw.get("price").replace(',', '.')) if odd_raw.get("price") != None else None
        } for odd_raw in odds_raw]

        return {
            "name": match_raw.get("desc"),
            "betId": match_raw.get("parent")[1:],
            "odd": odd,
        }
