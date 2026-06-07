import discord
import os
import sys
import yaml

from discord.ext import commands
from dotenv import load_dotenv
from logger import logger

load_dotenv()

try:
    with open('config.yml', 'r') as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    logger.critical("config.yml was not found or is missing from root directory.")
    sys.exit(1)
except yaml.YAMLError as e:
    logger.critical(f"Failed to parse config.yml, please check your syntax \nError: {e}")
    sys.exit(1)
    
intents = discord.Intents.default()
intents.message_content = True

token = os.getenv("DISCORD_TOKEN")
if not token:
    logger.critical("DISCORD_TOKEN is not set in the environment variables.")
    sys.exit(1)
    
class HavenBot(commands.Bot):
    async def setup_hook(self):
        for root,dirs,files in os.walk("Cogs",topdown=True):
            for file in files:
                if file.endswith(".py"):
                    cog_path = os.path.join(root, file[:-3]).replace(os.sep, ".")
                    try:
                        await self.load_extension(cog_path)
                        logger.info(f"Loaded Cog {file}")
                    except Exception as e:
                        logger.error(f"Failed to load Cog {cog_path}: {e}")
        
        
    async def on_ready(self):
        logger.info(f"Logged into Discord as {self.user} ({self.application_id})")
        logger.info(f"My prefix is set to: {self.config['prefix']}")
        
        status = discord.Activity(
            type=discord.ActivityType.playing,
            name=f"{len(self.guilds)} guilds | {config['prefix']}help"
            )
        
        await self.change_presence(status=discord.Status.online, activity=status)

bot = HavenBot(
    command_prefix=config['prefix'],
    help_command=None,
    intents=intents,
)
bot.config = config

try:
    bot.run(token, reconnect=True, log_handler=None)
except discord.PrivilegedIntentsRequired:
    logger.critical("One or more privileged intents are not enabled in the Discord Developer Portal.")
    sys.exit(1)
except discord.LoginFailure:
    logger.critical("An improper token has been passed. Please recheck DISCORD_TOKEN in the environment variables")
    sys.exit(1)