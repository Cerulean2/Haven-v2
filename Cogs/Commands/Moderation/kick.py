import discord
from discord.ext import commands

class KickFlags(commands.FlagConverter, prefix="--", delimiter=" "):
    reason: str = None
    
class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, flags: KickFlags):
        """Kicks a member from a guild."""
        
        if user == ctx.author:
            await ctx.reply("You should be kinder to yourself.")
            return
        
        if user.id == ctx.guild.me.id:
            await ctx.reply("I would prefer not to kick myself.")
            return
        
        if user.id == ctx.guild.owner_id:
            await ctx.reply("Trying to kick the owner? Bold move.")
            return
        
        if isinstance (user, discord.Member) and ctx.author.top_role <= user.top_role:
            await ctx.reply("Your role is not high enough to kick that member.")
            return
        
        if isinstance (user, discord.Member) and ctx.guild.me.top_role <= user.top_role:
            await ctx.reply("My role is not high enough to kick that member.")
            return
        
        await ctx.guild.kick(user, reason=flags.reason)
        await ctx.reply(f"✅ Successfully kicked {user.mention}")

async def setup(bot):
    await bot.add_cog(Kick(bot))