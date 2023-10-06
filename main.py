import discord
import os
from discord.ext import commands

class BOT:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.intents.typing = False
        self.intents.presences = False
        self.guild = ""
        self.bot = commands.Bot(command_prefix='!', intents=self.intents)

        @self.bot.tree.command(name="commandname", description="My first application Command", guild=discord.Object(id=env.GUILD_ID))  # Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
        async def first_command(interaction):
            await interaction.response.send_message("Hello!")
        @self.bot.event
        async def on_ready():
            guild_id = env.GUILD_ID
            print(type(guild_id))
            self.guild = self.bot.get_guild(guild_id)
            if self.guild is not None:
                await self.bot.tree.sync(guild=discord.Object(id=guild_id))
                print(f"Bot csatlakozott a következő szerverhez: {self.guild.name}")
            else:
                print("Nem található a szerver.")

        self.bot.run('env.DC_TOKEN')

BOT = BOT()