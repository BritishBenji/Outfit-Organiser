import discord
from discord.ext import commands
import json
from main import get_prefix, bot
import random


class ViewIndividual(commands.Cog):
    """
    This Cog allows you to view individual items
    """

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="I'm here to tell you what outfit to wear, ngl",
                       case_insensitive=True)

    @bot.command(name="view", description="View your Outfit!")
    async def Individual(self, ctx, *fit):
        outfits = {}

        with open("Outfits.json", "r") as myfile:
            outfits = json.load(myfile)

        fit = "".join(fit)

        fit = fit.replace("(", "")
        fit = fit.replace(")", "")
        fit = fit.replace(",", "")

        if fit == "":
            await ctx.send(f"Please Choose an Outfit first! View them with `{bot.command_prefix(bot, ctx)[2]}list`")
        else:
            if fit in outfits:
                embed = discord.Embed(title=f"Outfit {fit}", description="")
                embed.set_image(url=outfits.get(fit))
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=ctx.guild,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send(
                    f"That is not a listed Outfit! View your Outfits with `{bot.command_prefix(bot, ctx)[2]}list`")

    @bot.command(name="random", description="View a random Outfit!", aliases=["r"])
    async def Random(self, ctx):
        outfits = {}

        with open("Outfits.json", "r") as myfile:
            outfits = json.load(myfile)

        fit = random.choice(list(outfits.keys()))
        embed = discord.Embed(title=f"Your Random Outfit! \n{fit}")
        embed.set_image(url=outfits.get(fit))
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ViewIndividual(bot))
