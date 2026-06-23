import discord
import os
import aiohttp

from discord.ext import commands
from logger import logger

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        error = getattr(error, 'original', error)
        config = self.bot.config
        
        if isinstance(error, commands.MissingRequiredArgument):
            if ctx.command.qualified_name == "ban":
                embed = discord.Embed(title="Missing Argument", color=discord.Color.red())
                embed.description = (
                    f"**Usage:** `{ctx.prefix}ban <user> [flags]`\n"
                    f"**Flags:**\n"
                    f"`--reason` — reason for the ban\n"
                    f"`--days` — days of messages to delete (0-7)"
                )
                await ctx.reply(embed=embed)
            if ctx.command.qualified_name == "kick":
                embed = discord.Embed(title="Missing Argument", color=discord.Color.red())
                embed.description = (
                    f"**Usage:** `{ctx.prefix}kick <user> [flags]`\n"
                    f"**Flags:**\n"
                    f"`--reason` — reason for the kick\n"
                )
                await ctx.reply(embed=embed)
            if ctx.command.qualified_name == "pet":
                embed = discord.Embed(title="Missing Argument", color=discord.Color.red())
                embed.description = (
                    f"**Usage**: `{ctx.prefix}pet <user>`\n"
                )
                await ctx.reply(embed=embed)
            
        elif isinstance(error, commands.CommandNotFound):
            return # Dont log errors for CommandNotFound, its just unnecessary spam.
        
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title="Cooldown", color=discord.Color.red())
            embed.description = f"{error}"
            
            await ctx.reply(embed=embed)
    
        elif isinstance(error, commands.RangeError):
            embed = discord.Embed(title="Invalid Range", color=discord.Color.red())
            embed.description = f"{error}"
            
            await ctx.reply(embed=embed)
        
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(title="Missing Permissions", color=discord.Color.red())
            embed.description = f"{error}"
            
            await ctx.reply(embed=embed)
        
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Missing Permissions", color=discord.Color.red())
            embed.description = f"{error}"
            
            await ctx.reply(embed=embed)
        
        elif isinstance(error, commands.BadUnionArgument):
            embed = discord.Embed(title="Invalid Argument", color=discord.Color.red())
            embed.description = "Please mention a valid user or provide their user id."
                
            await ctx.reply(embed=embed)
        
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(title="Invalid Member", color=discord.Color.red())
            embed.description = "That's not a member of this guild. Please try a valid member."
                
            await ctx.reply(embed=embed)
        
        elif isinstance(error, aiohttp.client_exceptions.ClientConnectorError):
            if ctx.command.qualified_name == "cat":
                await ctx.reply("Sorry, there was an issue when I tried to communicate with the cat API. Please try again in a few minutes!")
                
            channel = self.bot.get_channel(int(config["error_channel"]))
            embed = discord.Embed(title="ClientConnectorError", color=discord.Color.red())
            embed.description = f"A bad thing happened when {ctx.author} (`{ctx.author.id}`) used `{ctx.command}` ```\n{error}\n```"
            
            if config['ping_errors'] == "true":
                await channel.send(content=f"<@{config['bot_owner']}>", embed=embed)
            else:
                await channel.send(embed=embed)
        
        else:
            if config['log_level'] == "DEBUG":
                logger.error("Exception in command '%s'", ctx.command, exc_info=error)
                
            channel = self.bot.get_channel(int(config["error_channel"]))
            embed = discord.Embed(title=f"{type(error).__name__}", color=discord.Color.red())
            embed.description = f"A bad thing happened when {ctx.author} (`{ctx.author.id}`) used `{ctx.command}` ```\n{error}\n```"
            await channel.send(embed=embed)
            
async def setup(bot):
    await bot.add_cog(Error(bot))