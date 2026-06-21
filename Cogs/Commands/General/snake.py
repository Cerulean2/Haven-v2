import discord
from discord.ext import commands

class Snake(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def snake(self, ctx):
        """Ssssssssnakes...."""
        await ctx.send("🐍 Ssssssssssssssss....")

async def setup(bot):
    await bot.add_cog(Snake(bot))