import discord
from discord.ext import commands
import json
from main import get_prefix


class Viewing(commands.Cog):
    """
    This Cog allows you to view your list of outfits
    """

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="I'm here to tell you what outfit to wear, ngl",
                       case_insensitive=True, help_command=None)

    @bot.command(name="list", description="Command to view a list of outfits")
    async def Viewing(self, ctx):
        ColdWeather = {}
        HotWeather = {}
        FullList = {}
        temp = []

        try:
            with open("ColdWeather.json", "r") as myfile:
                ColdWeather = json.load(myfile)
        except:
            pass
        try:
            with open("HotWeather.json", "r") as myfile:
                HotWeather = json.load(myfile)
        except:
            pass
        FullList = dict(ColdWeather, **HotWeather)
        names = list(FullList.keys())
        name = "\n".join(names)
        embed = discord.Embed(title="Here are your outfits!", description=name)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Viewing(bot))
