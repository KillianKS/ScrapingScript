import json
from datetime import datetime

from src.books.book import Book
from src.helpers.singleton_helper import SingletonHelper
from src.helpers.http_helper import HTTPHelper
from src.helpers.logger_helper import LoggerHelper


class Winamax(Book):
    EVENT_URL = "https://www.winamax.fr/paris-sportifs/match/{event}"


    def __init__(self, singleton_provider: SingletonHelper, config):
        super().__init__(singleton_provider, config)
        singleton_provider.has_singleton_or_exeption(HTTPHelper, LoggerHelper)

        self.http_service = singleton_provider.get_singleton(HTTPHelper)
        self.logger = singleton_provider.get_singleton(LoggerHelper)


    def get_sport_data(self, book_config):
        url = self._config["url"].format(id=book_config["id"])
        html = self.http_service.get(url).content
        bets = self.get_bets_from_page(html)
        if bets == None:
            return None
        return self.parse_bets(bets, book_config)


    def get_bets_from_page(self, html: str):
        START_STR = b"var PRELOADED_STATE = "
        END_STR = b";</script>"

        try:
            start_index = html.index(START_STR) + len(START_STR)
            end_index = html.index(END_STR, start_index)
            value = html[start_index:end_index].strip()
            if value:
                try:
                    return json.loads(value)
                except json.JSONDecodeError as e:
                    self.logger.error(ex, stack_info=True, exc_info=True)
        except Exception as ex:
            self.logger.error("Aucune valeur trouvée.")
            self.logger.error(ex, stack_info=True, exc_info=True)
        return None


    def parse_bets(self, parse_bets, book_config):
        matches_table = parse_bets.get("matches")
        if matches_table == None:
            self.logger.debug("No event")
            return None
        bets_table = parse_bets.get("bets")
        outcomes_table = parse_bets.get("outcomes")
        odds_table = parse_bets.get("odds")
        table_winamax = []
        for match in matches_table.values():
            match_bet_id = match.get("mainBetId")

            if match_bet_id != None and match.get("sportId") == int(book_config["id"]):
                cotes = []
                bet = bets_table.get(str(match_bet_id))
                bet_name = bet.get("betTitle")
                outcome_ids = bet.get("outcomes")
                bet_id = bet.get("betId")

                for outcome_id in [str(outcome_id) for outcome_id in outcome_ids]:
                    outcome = outcomes_table.get(outcome_id)
                    name_actor = outcome.get("label")
                    odd = odds_table.get(outcome_id)
                    cotes.append({ "player": name_actor, "cote": odd})

                table_winamax.append({
                    "event": match.get("matchId"),
                    "name": match.get("title"),
                    "bookmaker": "Winamax",
                    "sport": book_config["sport"],
                    "allBet4match": [{"name": bet_name, "betId": bet_id, "odd": cotes}],
                    "url": Winamax.EVENT_URL.format(event=match.get("matchId")),
                    "notify": None,
                    "expireAt": datetime.fromtimestamp(match.get("matchStart")).isoformat()
                })
        return table_winamax
