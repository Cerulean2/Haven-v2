import discord,logging

discord.utils.setup_logging(level=logging.INFO, root=True)
logger = logging.getLogger("havenbot")
