import discord
from discord.ext import commands

class BanFlags(commands.FlagConverter, prefix="--", delimiter=" "):
    reason: str = None
    days: commands.Range[int, 0, 7] = 0
    
class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member | discord.User, *, flags: BanFlags):
        """Bans a member from a guild."""
        
        if user == ctx.author:
            await ctx.reply("You should be kinder to yourself.")
            return
        
        if user.id == ctx.guild.me.id:
            await ctx.reply("I would prefer not to ban myself.")
            return
        
        if user.id == ctx.guild.owner_id:
            await ctx.reply("Trying to ban the owner? Bold move.")
            return
        
        if isinstance (user, discord.Member) and ctx.guild.me.top_role <= user.top_role:
            await ctx.reply("My role is not high enough to ban that member.")
            return
        
        await ctx.guild.ban(user, reason=flags.reason, delete_message_days=flags.days)
        await ctx.reply(f"👢 Banned `{user}`")

async def setup(bot):
    await bot.add_cog(Ban(bot))