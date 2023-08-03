import discord
from discord import app_commands

from src.database.database import Database
from src.helpers.configuration_helper import ConfigurationHelper
from src.helpers.logger_helper import LoggerHelper
from src.helpers.singleton_helper import SingletonHelper


class DiscordBotService(discord.Client):
    async def setup_hook(self):
        self.__tree.copy_global_to(guild=self.__guild)
        await self.__tree.sync(guild=self.__guild)


    def __init__(self, singleton_provider: SingletonHelper):
        super().__init__(intents=discord.Intents.default())
        singleton_provider.has_singleton_or_exeption(ConfigurationHelper, Database, LoggerHelper)

        self.__config = singleton_provider.get_singleton(ConfigurationHelper)
        self.__database = singleton_provider.get_singleton(Database)
        self.__logger = singleton_provider.get_singleton(LoggerHelper)

        self.__guild = discord.Object(id=int(self.__config.getConfig("DISCORD_GUILD")))
        self.__tree = app_commands.CommandTree(self)


        @self.__tree.command()
        @app_commands.describe()
        async def ping(interaction: discord.Interaction):
            """pong!"""
            await interaction.response.send_message('pong')


    def startBB(self):
        self.run(self.__config.getConfig("DISCORD_TOKEN"))
