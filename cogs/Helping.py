import discord
from discord.ext import commands

from main import get_prefix


class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="I'm here to tell you what outfit to wear, ngl",
                       case_insensitive=True, help_command=None)

    @bot.command(name="help", description="The Help Command!")
    async def help(self, ctx, *cog):
        """Gets all cogs and commands of mine."""
        if not cog:
            embed = discord.Embed(title='Cog Listing and Uncategorized Commands',
                                  description='Use `!help *cog*` to find out more about them!\n(BTW, the Cog Name '
                                              'Must Be in Title Case, Just Like this Sentence.)')
            cogs_desc = ''
            for x in self.bot.cogs:
                cogs_desc += ('{} - {}'.format(x,
                              self.bot.cogs[x].__doc__) + '\n')
            embed.add_field(
                name='Cogs', value=cogs_desc[0:len(cogs_desc) - 1], inline=False)
            cmds_desc = ''
            for y in self.bot.walk_commands():
                if not y.cog_name and not y.hidden:
                    cmds_desc += ('{} - {}'.format(y.name, y.help) + '\n')
                    embed.add_field(name='Uncategorized Commands', value=cmds_desc[0:len(
                        cmds_desc) - 1], inline=False)
            await ctx.message.add_reaction(emoji='✉')
            await ctx.message.author.send('', embed=embed)
        else:
            if len(cog) > 1:
                embed = discord.Embed(title='Error!', description='That is way too many cogs!',
                                      color=discord.Color.red())
                await ctx.message.author.send('', embed=embed)
            else:
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            embed = discord.Embed(title=cog[0] + ' Command Listing',
                                                  description=self.bot.cogs[cog[0]].__doc__)
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    embed.add_field(
                                        name=c.name, value=c.help, inline=False)
                            found = True
                if not found:
                    embed = discord.Embed(title='Error!', description='How do you even use "' + cog[0] + '"?',
                                          color=discord.Color.red())
                else:
                    await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send('', embed=embed)


def setup(bot):
    bot.add_cog(help(bot))
