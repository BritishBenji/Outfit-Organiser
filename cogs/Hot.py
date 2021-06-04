import discord
from discord.ext import commands
import json
from main import get_prefix, bot


# TODO: Allow categorisation by weather or smthn

class Hot(commands.Cog):
    """
    This Cog allows you to input your outfit choices for cold weather, hopefully also allowing you to input outfits with images
    """

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="I'm here to tell you what outfit to wear, ngl",
                       case_insensitive=True, help_command=None)

    @bot.command(name="hot", description="Command to input outfits for cold weather")
    async def Importing(self, ctx):
        outfits = {}
        try:
            with open('HotWeather.json') as myfile:
                outfits = json.load(myfile)
        except:
            pass

        # Embed for Outfit Name
        embed = discord.Embed(title="Add My Outfit!",
                              description="Please input the name of the outfit below!")
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

        # Get Outfit Name
        msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        msg = msg.content

        # Outfit Images
        embed = discord.Embed(title=f'Outfit: {msg}',
                              description='Please include a link to pictures of your outfits below!')
        await ctx.send(embed=embed)

        # Outfit Image Input (By Image Link to save space)
        msg2 = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        msg2 = msg2.content

        # Confirm Outfit
        embed = discord.Embed(title="You're about to create your outfit!",
                              description=f"You have named this outfit \"{msg}\"!")
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        embed.set_image(url=msg2)
        await ctx.send(embed=embed)

        # Long Winded way of confirming shit
        # TODO: Learn proper error handling to make this less messy?
        # TODO: Use message reactions instead
        
        while True:
            await ctx.send("Are you sure this is your outfit? (Please reply with `yes` or `no`)")
            yn = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            yn = yn.content
            if yn.lower() == "yes":
                outfits[msg] = msg2
                with open("HotWeather.json", "w") as myfile:
                    myfile.truncate(0)
                    json.dump(outfits, myfile)
                embed = discord.Embed(title="Outfit Saved!",
                                      description=f"To view your outfits, use the command `{bot.command_prefix(bot, ctx)[2]}list`")
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text=ctx.guild,
                                 icon_url=ctx.guild.icon_url)
                await ctx.send(embed=embed)
                break
            if yn.lower() == "no":
                await ctx.send("Outfit Creation has been cancelled!")
                break
            else:
                return


def setup(bot):
    bot.add_cog(Hot(bot))
