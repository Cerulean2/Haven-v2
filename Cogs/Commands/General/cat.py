import discord
import aiohttp
import os

from discord.ext import commands
from logger import logger
from environment import environment

class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_load(self):
        self.session = aiohttp.ClientSession()
    
    async def cog_unload(self):
        if self.session:
            await self.session.close()
        
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user) # Cooldown: 1 request every 10 seconds per user
    async def cat(self, ctx):
        """Returns a random cat image"""
        url = environment.kat_api_url
        cat_url = None
        
        if not url:
            logger.error("Error during cat command: KAT_API_URL is not set in the environment variables.")
            await ctx.reply("My environment is missing the url for the cat API. Please inform the bot owner about this.")
            return
        
        try:
            async with self.session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                data = await response.json()
                cat_url = data.get("url")
                
        except Exception as e:
            logger.error(f"Error with Kat API: {e}")
        
        if not cat_url:
            await ctx.reply("Sorry, the API response didn't return an image url. Please try again.")
            return
        
        embed = discord.Embed()
        embed.set_image(url=cat_url)
        
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Cat(bot))