import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

class HavenBot(commands.Bot):
    async def setup_hook(self):
        for file in os.listdir(path="Commands/General"):
            if file.endswith(".py"):
                await self.load_extension(f"Commands.General.{file[:-3]}")
                print(f"Loaded Cog {file}")
    
    async def on_ready(self):
        print(f"Logged into Discord as {self.user} ({self.application_id})")

bot = HavenBot(
    command_prefix='h.',
    help_command=None,
    intents=intents
)

bot.run(os.getenv("DISCORD_TOKEN"))