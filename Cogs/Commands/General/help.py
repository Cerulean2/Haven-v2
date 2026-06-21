import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx):
        """Help message"""
        config = self.bot.config
        
        embed = discord.Embed(title="────────────────────────────────────────",
                      colour=0x0080c0)

        embed.set_author(name="Haven Commands",
                        icon_url="https://cdn.discordapp.com/avatars/1506465698124267552/a831a42e05a844a560846c0de81fe9bf.png?size=4096")
        
        embed.add_field(name="**General**",
                        value=f"""
                        `{config['prefix']}help` - Shows this command.
                        \n`{config['prefix']}ping` - Returns the bots latency.
                        \n`{config['prefix']}cat` - Sends a random cat gif.
                        \n`{config['prefix']}snake` - Sssssss....
                        \n`{config['prefix']}snipe` - Snipes a recently deleted message.
                        """,
                        inline=True)
        
        embed.add_field(name="**Moderation**",
                        value=f"""
                        `{config['prefix']}ban` - Bans a member from the guild.
                        \n`{config['prefix']}kick` - Kicks a member from the guild.
                        """,
                        inline=True)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))