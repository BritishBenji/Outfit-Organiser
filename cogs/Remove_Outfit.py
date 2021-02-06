import discord
from discord.ext import commands
import json
from main import get_prefix, bot


class Removing(commands.Cog):
    """
    This Cog allows you to remove one of your previously added outfits
    """

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="I'm here to tell you what outfit to wear, ngl",
                       case_insensitive=True)

    @bot.command(name="remove", description="Command to remove outfits", aliases=["del", "rem", "delete"])
    async def Removing(self, ctx, *fit):
        outfits = {}
        temp = []

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
                embed = discord.Embed(title=f"Do you wish to delete Outfit: {fit}?", description="")
                embed.set_image(url=outfits.get(fit))
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=ctx.guild,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)
                yn = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                yn = yn.content
                del outfits[fit]
                if yn.lower() == "yes":
                    with open("Outfits.json", "w") as myfile:
                        myfile.truncate(0)
                        json.dump(outfits, myfile)
                    embed = discord.Embed(title=f"Outfit: {fit} has been removed", description="")
                    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                    embed.set_footer(text=ctx.guild,
                                     icon_url=ctx.guild.icon_url)
                    await ctx.send(embed=embed)

                if yn.lower() == "no":
                    await ctx.send("Operation Cancelled")
            else:
                await ctx.send(
                    f"That is not a listed Outfit! View your Outfits with `{bot.command_prefix(bot, ctx)[2]}list`")


def setup(bot):
    bot.add_cog(Removing(bot))
