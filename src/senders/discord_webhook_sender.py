from datetime import datetime

from src.helpers.configuration_helper import ConfigurationHelper
from src.helpers.singleton_helper import SingletonHelper
from src.helpers.webhook_helper import WebhookHelper
from src.senders.sender import Sender


class DiscordWebHookSender(WebhookHelper, Sender):
    # TODO? add it in the mongo db ?
    BOOKS_CUSTOM = {
        "Winamax": "https://operator-front-static-cdn.winamax.fr/img/content/poker/2022/20220412_logo_winamax/LogoWinamax2022_v2.png",
        "Betclic": "https://play-lh.googleusercontent.com/Kw5Ec424gSMm5gKoXhpoZ28xGe8umSowL5phPX5zuwbKwk9Q6bbgxW5MTR39ObaeWg=w240-h480-rw",
        "Unibet": "https://play-lh.googleusercontent.com/F3EheSGFcNsukoS30hjs8eMahfb5FiaU0DIAnpoVZKv4KZ5QXDd6guZVk4MLpkXOwgKX=s48-rw",
        "Zebet": "https://media.sportsight.co.uk/fig/app/uploads/2019/12/09190111/zebet_300x300.png"
    }

    SPORTS_CUSTOM = {
        "Ski Alpin": { "color": 16579836, "img" : "https://www.challenges.fr/assets/img/2022/09/05/cover-r4x3w1200-6315fa952d3a7-b3572ef09025f6258c4ffdf5290c8d7122916dd2-jpg.jpg" },
        "Biathlon": { "color": 13761923, "img": "https://www.womensports.fr/wp-content/uploads/2022/11/Icon_0000540829_HiRes_00K05FL0YDSLXC0X1NDDS00RO4JL-750x500.jpg"},
        "Ski de fond": { "color": 9145227, "img" : "https://france3-regions.francetvinfo.fr/image/Ek-lbtNHouUFesm-JMJg5gJi9-I/600x400/regions/2023/01/12/63c032ce60050_epalivesix584758.jpg" },
        "Athlétisme": { "color": 5542638, "img" : "https://images.lindependant.fr/api/v1/images/view/5a95aa6e8fe56f6e6310ba69/large/image.jpg" },
        "Natation": { "color": 8531, "img" : "https://media2.ledevoir.com/images_galerie/nwd_966618_778866/image.jpg" },
        "Cyclisme": { "color": 16771840, "img" : "https://www.francetvinfo.fr/pictures/bhBp1Q7Hxa2en-z-2tj3ePNujUw/432x243/2023/06/15/648b0cca30d48_maxsportsfrtwo744019.jpg" },
        "Golf": { "color": 16190476, "img" : "https://blog.visitacostadelsol.com/hubfs/1-Mar-31-2021-03-05-26-33-PM.jpg" },
        "Tennis": { "color": 16088832, "img" : "https://www.ergysport.com/wp-content/uploads/2017/03/tennis-ergysport-1-820x566.jpg" },
        "Basketball": { "color": 16088832, "img": "https://www.ncaa.org/images/2023/3/30/MBB-WBB_BallHoop.JPG?width=942&quality=80&format=jpg" }
        # "Auto-moto (peut s'appeler Formule 1, Nascar, Moto GP, Endurance - sur les sites de paris)"      "⛽" : 4335616
    }


    def __init__(self, singleton_provider: SingletonHelper) -> None:
        singleton_provider.has_singleton_or_exeption(ConfigurationHelper)
        config = singleton_provider.get_singleton(ConfigurationHelper)

        super().__init__(config.getConfig("DISCORD_WEBHOOK"))


    def format_match(self, bdd_match):
        sport_custom = self.SPORTS_CUSTOM[bdd_match["sport"]]

        expire_at = datetime.strptime(bdd_match["expireAt"], '%Y-%m-%dT%H:%M:%S').strftime("%m/%d/%Y %H:%M:%S")

        return {
            "embeds": [{
                "title": bdd_match["name"],
                "url": bdd_match["url"],
                "color": sport_custom["color"],
                "author": {
                    "name": "{} - {}".format(bdd_match["sport"], expire_at)
                },
                "fields": [{
                    "name": bet["name"],
                    "value": '\n'.join(["* {}\n * {}".format(odd["player"], odd["cote"]) for odd in bet["odd"]]) + '\n'
                } for bet in bdd_match["allBet4match"]],
                "footer": {
                    "text": "VPSolutions"
                },
                "thumbnail": {
                "url": sport_custom["img"]
                }
            }],
            "username": bdd_match["bookmaker"],
            "avatar_url": self.BOOKS_CUSTOM[bdd_match["bookmaker"]]
        }
