# Outfit picking program for the Weeb
# "Always assume the end-user is a complete asshole" -
# Michael Reeves, 17 Aug 2017

# TODO: fix shit
# TODO: Allow outfits to be categorized based on weather
# TODO: Allow outfits to be picked at random
# TODO: Create Cog for removing Outfits

import os
import discord
from discord.ext import commands


guilds = []
directory = os.getcwd()


def get_prefix(client, message):
    prefixes = ['!!']  # sets the prefixes, you can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['!']  # Only allow '!' as a prefix when in DMs, this is optional

    return commands.when_mentioned_or(*prefixes)(client, message)


# Set's out your prefix, and shortens the module name waaayyyyyy down. Pretty nifty, ngl
bot = commands.Bot(command_prefix=get_prefix, description="I'm here to tell you what outfit to wear, ngl",
                   case_insensitive=True)

# FIXME: Help Command
# bot.remove_command('help')

# collect token here
file1 = open(f"{directory}\\token.txt", "r")
TOKEN = file1.readlines()
file1.close()
TOKEN = " ".join(TOKEN)

global outfits


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    while len(guilds) < 1:
        async for guild in bot.fetch_guilds(limit=150):
            guilds.append(guild.name)
    print(guilds)
    await bot.change_presence(
        activity=discord.Streaming(name="In Development!", url="https://www.twitch.tv/BritishBenji"))
    user = bot.user
    await user.edit(nick="What do I Wear Today?")


# Loads the cogs, prints them out, self explanatory I guess
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'cogs.{filename}')


bot.run(TOKEN, bot=True, reconnect=True)
