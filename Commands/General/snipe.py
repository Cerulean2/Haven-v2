import discord
from discord.ext import commands

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.deleted_messages = {}
    
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author.bot:
            return
        
        self.deleted_messages[message.channel.id] = {
            "author": str(message.author),
            "author_avatar": message.author.display_avatar.url,
            "content": message.content,
            "attachments": message.attachments,
            "created_at": discord.utils.utcnow()
        }
        
    @commands.command()
    async def snipe(self, ctx):
        """Retrieve a recently deleted message from the channel."""
        data = self.deleted_messages.get(ctx.channel.id)

        if not data:
            await ctx.reply("There are no messages to snipe.")
        

        embed = discord.Embed(
            color=discord.Color.dark_blue(),
            description=data["content"], 
            timestamp=data["created_at"]
        )
        
        embed.set_author(
            name=data["author"], 
            icon_url=data["author_avatar"]
        )

        if data["attachments"]:
            image = data["attachments"][0] # Only set first attachment

            embed.set_image(url=image)

        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Snipe(bot))