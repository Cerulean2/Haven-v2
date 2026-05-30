import discord
import os
import sys

from discord.ext import commands
from dotenv import load_dotenv
from logger import logger

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

class HavenBot(commands.Bot):
    async def setup_hook(self):
        for file in os.listdir(path="Commands/General"):
            if file.endswith(".py"):
                try:
                    await self.load_extension(f"Commands.General.{file[:-3]}")
                    logger.info(f"Loaded Cog {file}")
                except Exception as e:
                    logger.error(f"Failed to log Cog {file[:-3]}: {e}")
    
    async def on_ready(self):
        logger.info(f"Logged into Discord as {self.user} ({self.application_id})")
        
        status = discord.Activity(
            type=discord.ActivityType.playing,
            name=f"{len(self.guilds)} guilds | h.help"
            )
        
        await self.change_presence(status=discord.Status.online, activity=status)

bot = HavenBot(
    command_prefix='h.',
    help_command=None,
    intents=intents,
)

token = os.getenv("DISCORD_TOKEN")
if not token:
    logger.critical("DISCORD_TOKEN is not set in the environment variables.")
    sys.exit(1)

bot.run(token, log_handler=None)