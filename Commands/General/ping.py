import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):
        """Pong! Sends the current latency of Haven."""
        await ctx.send("Pong! `{0}ms`".format(round(self.bot.latency * 1000)))

async def setup(bot):
    await bot.add_cog(General(bot))