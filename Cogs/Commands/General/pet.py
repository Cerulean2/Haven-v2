import discord
import aiohttp, asyncio
import io

from discord.ext import commands
from logger import logger
from environment import environment

class PetPet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_load(self):
        self.session = aiohttp.ClientSession()
    
    async def cog_unload(self):
        if self.session:
            await self.session.close()
        
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user) # Cooldown: 1 request every 10 seconds per user
    async def pet(self, ctx, user: discord.Member | discord.User):
        """Generates a petpet gif directly from an image URL."""
        
        if not environment.pet_api_url:
            logger.error("Error during pet command: PET_API_URL is not set in the environment variables.")
            await ctx.reply("My environment is misconfigured and cannot reach the petpet API. Please inform the bot owner about this.")
            return
        
        status_message = await ctx.reply("📞 Please hold. Your call is very important to us.")
        
        discord_file = None
        userAvatarUrl = user.avatar.url
        url = f"{environment.pet_api_url}?image={userAvatarUrl}"

        try:
            async with self.session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status != 200:
                    await status_message.edit(content="The petpet API returned an error. Please try again later.")
                    return
                
                data = await response.read()
                file_stream = io.BytesIO(data)
                discord_file = discord.File(file_stream, filename="petpet.gif")
                
        except asyncio.TimeoutError:
            await ctx.reply("The petpet API took too long to respond. Please try again in a few moments!")
            return
        
        except aiohttp.ClientError as e:
            await status_message.edit(content="Could not connect to the petpet generation service right now.")
            logger.error(f"Network error in pet command: {e}")
            return
        
        if not discord_file:
            await status_message.edit(content="Sorry, I wasn't able to get a petpet gif. Please try again in a few minutes.")
            return
        
        await status_message.edit(content=None, attachments=[discord_file])

async def setup(bot):
    await bot.add_cog(PetPet(bot))