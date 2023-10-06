"""Module providing a function printing python version."""
import discord
from discord.ext import commands

class BOT: # pylint: disable=too-few-public-methods
    """Class representing a Bot"""
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.intents.typing = False
        self.intents.presences = False
        self.guild = None
        self.bot = commands.Bot(command_prefix='!', intents=self.intents)

        @self.bot.tree.command(name="commandName",
                               description="My first application Command",
                               guild=discord.Object(id=9))
        async def first_command(interaction):
            await interaction.response.send_message("Hello!")

        @self.bot.event
        async def on_ready():
            guild_id = 9
            self.guild = self.bot.get_guild(guild_id)
            if self.guild is not None:
                await self.bot.tree.sync(guild=discord.Object(id=guild_id))
                print(f"Bot csatlakozott a következő szerverhez: {self.guild.name}")
            else:
                print("Nem található a szerver.")


if __name__ == "__main__":
    BOT().bot.run("a")
