import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx):
        """No help."""
        await ctx.send("No help.")

async def setup(bot):
    await bot.add_cog(Help(bot))