import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx):
        """Help message"""
        config = self.bot.config
        
        await ctx.reply(f"We're out of help right now. Try using a command like `{config['prefix']}ban` for usage.")

async def setup(bot):
    await bot.add_cog(Help(bot))