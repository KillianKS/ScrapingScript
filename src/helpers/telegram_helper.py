import requests as req


class TelegramHelper():
    __URL_SEND_MSG = "https://api.telegram.org/bot{}/sendMessage"


    def __init__(self, token: str, default_chat_id: str):
        self.__token = token
        self.__default_chat_id = default_chat_id


    def send(self, msg: str, chat_id: str=None) -> bool:
        data = {
            "chat_id": self.__default_chat_id if chat_id == None else chat_id,
            "parse_mode": "HTML",
            "text": msg
        }
        msg = req.post(TelegramHelper.__URL_SEND_MSG.format(self.__token), data=data)

        return msg.status_code == req.codes.ok
