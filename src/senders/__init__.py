from src.senders.sender import Sender
from src.senders.discord_webhook_sender import DiscordWebHookSender
from src.senders.telegram_sender import TelegramSender


# TODO: Add new sender class here
SENDERS_CLASS: list[Sender] = [DiscordWebHookSender] #, TelegramSender]