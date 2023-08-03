from src.helpers.singleton_helper import SingletonHelper
from src.helpers.configuration_helper import ConfigurationHelper
from src.helpers.telegram_helper import TelegramHelper
from src.senders.sender import Sender


class TelegramSender(TelegramHelper, Sender):
    def __init__(self, singleton_provider: SingletonHelper):
        singleton_provider.has_singleton_or_exeption(ConfigurationHelper)
        config = singleton_provider.get_singleton(ConfigurationHelper)

        token = config.getConfig("TELEGRAM_TOKEN")
        default_channel = config.getConfig("TELEGRAM_CHANNEL")
        super().__init__(token, default_channel)


    def format_match(self, match):
        msgText = f'<a href="https://{match["bookmaker"]}.fr{match["url"]}"><b>{match["bookmaker"]}</b></a> <i>{match["sport"]}</i>: {match["name"]} :\n'

        for odd in match['allBet4match']:
            oddText = ''
            for o in odd["odd"]:
                oddText += f' {o["player"]} : <b>{o["cote"]}</b>'
            msgText += '- ' + odd["name"] + \
                ' @ <i>' + oddText + "</i>\n"
        return msgText