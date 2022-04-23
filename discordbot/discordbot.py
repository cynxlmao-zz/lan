import os
from discord.ext import commands
import discord
import dotenv
import pytz
from datetime import datetime
import random
import requests
from cogs.admin import Admin
from cogs.nsfw import Nsfw
from cogs.normalcommands import NormalCommands
from cogs.events import Events
from cogs.help import Help

dotenv.load_dotenv()

bot = commands.Bot(command_prefix=';', help_command=None)
print("Logging in...")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        e = discord.Embed(title="Error", description=f"""{ctx.author.mention}, that command doesn't exist!
        Did you misspell the command?\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)
    elif isinstance(error, commands.MissingRequiredArgument):
        e = discord.Embed(title="Error", description=f"""{ctx.author.mention}, you are missing a required argument!\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)
    elif isinstance(error, commands.CommandOnCooldown):
        e = discord.Embed(title="Error", description=f"""{ctx.author.mention}, you're sending commands too fast!
        Slow down! Cooldowns last either 3 seconds or 10.\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)
    elif isinstance(error, commands.NSFWChannelRequired):
        e = discord.Embed(title="Error", description=f"""{ctx.author.mention}, this command can only be used in NSFW channels!\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)

bot.add_cog(Events(bot))
bot.add_cog(Help(bot))
bot.add_cog(NormalCommands(bot))
bot.add_cog(Nsfw(bot))
bot.add_cog(Admin(bot))

bot.run(os.getenv("TOKEN"))
