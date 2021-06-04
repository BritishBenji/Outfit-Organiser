import json
import random

import discord
from discord.ext import commands
from main import bot, get_prefix

from cogs.Cold import Cold


class ViewIndividual(commands.Cog):
    """
    This Cog allows you to view individual items, either at random, or a specific outfit
    """

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="I'm here to tell you what outfit to wear, ngl",
                       case_insensitive=True, help_command=None)

    @bot.command(name="view", description="View your Outfit!")
    async def Individual(self, ctx, *fit):
        ColdWeather = {}
        HotWeather = {}
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
        # I know I fucked something up for it to be like this, but it works for now I guess
        fit = " ".join(fit)

        fit = fit.replace("(", "")
        fit = fit.replace(")", "")
        fit = fit.replace(",", "")

        if fit == "":
            await ctx.send(f"Please Choose an Outfit first! View them with `{bot.command_prefix(bot, ctx)[2]}list`")
        else:
            if fit in ColdWeather.keys():
                embed = discord.Embed(title=f"Outfit {fit}", description="")
                embed.set_image(url=ColdWeather.get(fit))
                embed.set_author(name=ctx.message.author,
                                 icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=ctx.guild,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)
            if fit in HotWeather.keys():
                embed = discord.Embed(title=f"Outfit {fit}", description="")
                embed.set_image(url=HotWeather.get(fit))
                embed.set_author(name=ctx.message.author,
                                 icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=ctx.guild,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)
            # Commenting this out as for some reason it runs with an else too?
            """
            if fit not in HotWeather.keys() or ColdWeather.keys():
                await ctx.send(
                    f"That is not a listed Outfit! View your Outfits with `{bot.command_prefix(bot, ctx)[2]}list`")
            """

    @bot.command(name="random", description="View a random Outfit!", aliases=["r"])
    async def Random(self, ctx, *weather):
        ColdWeather = {}
        HotWeather = {}
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
        if weather == None:
            a = random.randint(0, 1)
            if a == 1:
                fit = random.choice(list(HotWeather.keys()))
                embed = discord.Embed(title=f"Your Random Outfit! \n{fit}")
                embed.set_image(url=HotWeather.get(fit))
                embed.set_author(name=ctx.message.author,
                                 icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=ctx.guild,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)
            if a == 0:
                fit = random.choice(list(ColdWeather.keys()))
                embed = discord.Embed(title=f"Your Random Outfit! \n{fit}")
                embed.set_image(url=ColdWeather.get(fit))
                embed.set_author(name=ctx.message.author,
                                 icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=ctx.guild,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)

        if weather[0].lower() == "hot":
            fit = random.choice(list(HotWeather.keys()))
            embed = discord.Embed(title=f"Your Random Outfit! \n{fit}")
            embed.set_image(url=HotWeather.get(fit))
            embed.set_author(name=ctx.message.author,
                             icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
        if weather[0].lower() == "cold":
            fit = random.choice(list(ColdWeather.keys()))
            embed = discord.Embed(title=f"Your Random Outfit! \n{fit}")
            embed.set_image(url=ColdWeather.get(fit))
            embed.set_author(name=ctx.message.author,
                             icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
        elif weather[0].lower != "hot" or "cold":
            await ctx.send("Please only use hot or cold as arguments!")


def setup(bot):
    bot.add_cog(ViewIndividual(bot))
