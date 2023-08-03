from src.database.database import Database
from src.helpers.singleton_helper import SingletonHelper


class LocalDatabase(Database):
    def __init__(self, singleton_provider: SingletonHelper):
        pass


    def upsert_event(self, event):
        print(f"{event.get('bookmaker')}: {event.get('sport')}: {event.get('event')}")


    def event_is_notify(self, eventId):
        pass


    def get_actives_books_config(self):
        return [book_config for book_config in [
            {
                "name": "Unibet",
                "isActive": False,
                "bookConfig": [
                    {
                        "sport": "Hiver",
                        "id": 675043280,
                        "filtre": "Compétition&marketname=Vainqueur de l'épreuve",
                        "isActive": False
                    },
                    {
                        "sport": "Hiver top 2",
                        "id": 675043280,
                        "filtre": "Compétition&marketname=Top 10",
                        "isActive": False
                    },
                    {
                        "sport": "SuperCote",
                        "id": "703695152",
                        "filtre": "Super Cote Boostée&marketname=Super Cote Boostée (50€ max)",
                        "isActive": True
                    },
                    {
                        "sport": "Tennis",
                        "id": "16883585",
                        "filtre": "Résultat&marketname=Vainqueur du match",
                        "isActive": True
                    },
                    {
                        "sport": "FootBall Global",
                        "id": 2243762,
                        "filtre": "Résultat&marketname=Résultat du match",
                        "isActive": False
                    },
                    {
                        "sport": "FootBall Europeen Only",
                        "id": 126968347,
                        "filtre": "Résultat&marketname=Résultat du match",
                        "isActive": False
                    },
                    {
                        "sport": "Basketball",
                        "id": 30769271,
                        "filtre": "Résultat&marketname=Vainqueur du match (prolong. incluses)",
                        "isActive": False
                    },
                    {
                        "sport": "Auto-Moto",
                        "id": "2741783",
                        "filtre": "Course&marketname=Vainqueur de la course",
                        "isActive": True
                    },
                    {
                        "sport": "Badminton",
                        "id": 30485980,
                        "filtre": "Résultat&marketname=Vainqueur du match",
                        "isActive": False
                    },
                    {
                        "sport": "Baseball MLB",
                        "id": 2640509,
                        "filtre": "Résultat&marketname=Vainqueur du match",
                        "isActive": False
                    },
                    {
                        "sport": "Boxe Global",
                        "id": 254514364,
                        "filtre": "Résultat&marketname=Vainqueur du combat",
                        "isActive": False
                    },
                    {
                        "sport": "Boxe/MMA Global",
                        "id": 6060135,
                        "filtre": "Résultat&marketname=Vainqueur du combat",
                        "isActive": False
                    },
                    {
                        "sport": "Cyclisme",
                        "id": "46582804",
                        "filtre": "Compétition&marketname=Vainqueur de la compétition",
                        "isActive": True
                    },
                    {
                        "sport": "Football Américain",
                        "id": 33519287,
                        "filtre": "Résultat&marketname=Vainqueur (Prolongations incluses)",
                        "isActive": False
                    },
                    {
                        "sport": "Football Australien",
                        "id": 702556721,
                        "filtre": "Résultat&marketname=Vainqueur du match",
                        "isActive": False
                    },
                    {
                        "sport": "Golf",
                        "id": 2116292,
                        "filtre": "Compétition&marketname=Vainqueur de la compétition",
                        "isActive": False
                    },
                    {
                        "sport": "Handball",
                        "id": 11331239,
                        "filtre": "Résultat&marketname=Résultat du match",
                        "isActive": False
                    },
                    {
                        "sport": "Hockey",
                        "id": 2702713,
                        "filtre": "Résultat&marketname=Résultat du match",
                        "isActive": False
                    },
                    {
                        "sport": "MMA",
                        "id": 703695306,
                        "filtre": "Résultat&marketname=Vainqueur du combat (2 possibilités)",
                        "isActive": False
                    },
                    {
                        "sport": "Rugby XV",
                        "id": 798481,
                        "filtre": "Résultat&marketname=Résultat du match",
                        "isActive": False
                    },
                    {
                        "sport": "Rugby XIII Superleague anglaise",
                        "id": 30359680,
                        "filtre": "Résultat&marketname=Résultat du match",
                        "isActive": False
                    },
                    {
                        "sport": "Rugby XII Superleague Anglaise",
                        "id": 30956841,
                        "filtre": "Résultat&marketname=Résultat du match",
                        "isActive": False
                    },
                    {
                        "sport": "Snooker",
                        "id": 198661952,
                        "filtre": "Compétition&marketname=Vainqueur de la compétition",
                        "isActive": False
                    },
                    {
                        "sport": "Sport Hive Global",
                        "id": "675043280",
                        "filtre": "Résultat&marketname=Vainqueur",
                        "isActive": False
                    },
                    {
                        "sport": "Biathlon",
                        "id": 675066649,
                        "filtre": "Compétition&marketname=Vainqueur de la compétition",
                        "isActive": False
                    },
                    {
                        "sport": "Ski alpin",
                        "id": 675066668,
                        "filtre": "Compétition&marketname=Vainqueur de la compétition",
                        "isActive": False
                    },
                    {
                        "sport": "Volleyball",
                        "id": 992098,
                        "filtre": "Résultat&marketname=Vainqueur du match",
                        "isActive": False
                    },
                    {
                        "sport": "Beach-Volley",
                        "id": 30501459,
                        "filtre": "Résultat&marketname=Vainqueur du match",
                        "isActive": False
                    },
                    {
                        "sport": "Water Polo",
                        "id": 29866078,
                        "filtre": "Compétition&marketname=Vainqueur de la compétition",
                        "isActive": False
                    },
                    {
                        "sport": "Ski de fond",
                        "id": "675066750",
                        "isActive": False,
                        "filtre": "Résultat&marketname=Vainqueur"
                    },
                    {
                        "sport": "Tennis Match",
                        "id": "116906728",
                        "isActive": True,
                        "filtre": "Résultat&marketname=Vainqueur du match"
                    },
                    {
                        "sport": "Athlétisme",
                        "id": "305157226",
                        "isActive": True,
                        "filtre": "Compétition&marketname=Vainqueur de l'épreuve"
                    }
                ],
                "url": "https://unibet.fr/zones/v3/sportnode/markets.json?nodeId={id}&filter={filtre}"
            },
            {
                "name": "Betclic",
                "isActive": False,
                "bookConfig": [
                    {
                        "sport": "Football",
                        "id": 1,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Tennis",
                        "id": "2",
                        "isActive": True,
                        "filtre": "2013"
                    },
                    {
                        "sport": "Test-Matchs",
                        "id": 172,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "NRL",
                        "id": 2808,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "NBA",
                        "id": "1115",
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "WNBA",
                        "id": 513,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Basket-ball",
                        "id": 4,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "NFL",
                        "id": 84,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "NHL",
                        "id": 83,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Baseball",
                        "id": 20,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Handball",
                        "id": 9,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Volley-ball",
                        "id": 8,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Cyclisme",
                        "id": "6",
                        "isActive": True,
                        "filtre": "3716"
                    },
                    {
                        "sport": "Golf",
                        "id": 7,
                        "isActive": False,
                        "filtre": "2652"
                    },
                    {
                        "sport": "Moto",
                        "id": 15,
                        "isActive": True,
                        "filtre": "1874"
                    },
                    {
                        "sport": "Nascar",
                        "id": 24,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Speedway",
                        "id": 55,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Water-polo",
                        "id": 33,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Boxe",
                        "id": 16,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "UFC",
                        "id": 15946,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "MMA",
                        "id": 23,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "AFL",
                        "id": 5524,
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "SkiAlpin",
                        "id": "18",
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Biathlon",
                        "id": "62",
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "SkiAcrobatique",
                        "id": "68",
                        "isActive": False,
                        "filtre": ""
                    },
                    {
                        "sport": "Athlétisme",
                        "id": "26",
                        "isActive": True,
                        "filtre": "2214"
                    }
                ],
                "url": "https://offer.cdn.begmedia.com/api/pub/v4/sports/{id}?application=2&countrycode=fr&hasSwitchMtc=True&language=fr&limit=999&markettypeId={filter}&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate"
            },
            {
                "name": "PMU",
                "isActive": False,
                "bookConfig": [
                    {
                        "sport": "Rugby à 13",
                        "id": "rugby13",
                        "isActive": True
                    },
                    {
                        "sport": "Tennis",
                        "id": "tennis",
                        "isActive": True
                    },
                    {
                        "sport": "Basketball US",
                        "id": "basketballus",
                        "isActive": True
                    },
                    {
                        "sport": "Basketball EU",
                        "id": "basketballeu",
                        "isActive": True
                    },
                    {
                        "sport": "Handball",
                        "id": "handball",
                        "isActive": True
                    },
                    {
                        "sport": "Volleyball",
                        "id": "volleyball",
                        "isActive": True
                    },
                    {
                        "sport": "Cyclisme",
                        "id": "cyclisme",
                        "isActive": True
                    },
                    {
                        "sport": "Natation",
                        "id": "natation",
                        "isActive": True
                    },
                    {
                        "sport": "Hockey-sur-glace EU",
                        "id": "hockeyeu",
                        "isActive": True
                    },
                    {
                        "sport": "Hockey-sur-glace US",
                        "id": "hockeyus",
                        "isActive": True
                    },
                    {
                        "sport": "Football",
                        "id": "football",
                        "isActive": False
                    }
                ],
                "url": "https://www.eficiens-serving2.com/pmu/ageban/extended/flex-xml/partenaires/vpronos/m77ocmfozs31/{id}.xml"
            },
            {
                "name": "Zebet",
                "bookConfig": [
                    {
                        "sport": "Tennis",
                        "id": "21-tennis",
                        "isActive": True
                    },
                    {
                        "sport": "Formule 1",
                        "id": "32-formule_1",
                        "isActive": True
                    },
                    {
                        "sport": "Sport Automobile",
                        "id": "19-sport_automobile",
                        "isActive": True
                    },
                    {
                        "sport": "Moto",
                        "id": "33-moto",
                        "isActive": True
                    },
                    {
                        "sport": "Golf",
                        "id": "18-golf",
                        "isActive": True
                    },
                    {
                        "sport": "Super Cotes",
                        "id": "71-super_cotes",
                        "isActive": True
                    }
                ],
                "isActive": True,
                "url": "https://www.zebet.fr/fr/sport/{id}"
            },
            {
                "name": "Winamax",
                "bookConfig": [
                    {
                        "sport": "Basketball",
                        "id": "2",
                        "isActive": True
                    }
                ],
                "isActive": True,
                "url": "https://www.winamax.fr/paris-sportifs/sports/{id}"
            },
            {
                "name": "Parionssport",
                "bookConfig": [
                    {
                        "sport": "Tennis",
                        "id": "239",
                        "isActive": True
                    }
                ],
                "isActive": True,
                "url": "https://www.enligne.parionssport.fdj.fr/lvs-api/next/50/p{id}"
            }
        ] if book_config.get("isActive")]


    def get_not_notify_events(self):
        return []