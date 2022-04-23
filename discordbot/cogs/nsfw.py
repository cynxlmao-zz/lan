import discord
import requests
import random
from discord.ext import commands

class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hentai(self, ctx):
        r = requests.get("https://nekos.life/api/lewd/neko").json()['neko']
        e = discord.Embed(description="This bot is still in beta. DM `cynx#9038` if there are any problems.")
        e.set_image(url=r)
        await ctx.reply(embed=e)

    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def femboy(self, ctx):
        r = requests.get("https://www.reddit.com/r/femboy/new.json?sort=hot", headers={"User-Agent": "sjflkdjsflsdj"})
        res = r.json()
        e = discord.Embed(description="""This bot is still in beta. DM `cynx#9038` if there are any problems.
        Fixing problem where nothing shows ASAP :)""")
        url = res['data']['children'][random.randint(0, 25)]['data']['url']
        e.set_image(url=url)
        await ctx.reply(embed=e)

    @commands.command(aliases = ['sex'])
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def porn(self, ctx):
        r = requests.get("https://www.reddit.com/r/pornpics/new.json?sort=hot", headers={"User-Agent": "sjflkdjsflsdj"})
        res = r.json()
        e = discord.Embed(description="""This bot is still in beta. DM `cynx#9038` if there are any problems.
		Fixing problem where nothing shows ASAP :)""")
        url = res['data']['children'][random.randint(0, 25)]['data']['url']
        e.set_image(url=url)
        await ctx.reply(embed=e)

    @commands.command(aliases=['homo','lesbian'])
    @commands.is_nsfw()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gay(self, ctx):
        r = requests.get("https://www.reddit.com/r/LGBTGoneWild/new.json?sort=hot", headers={"User-Agent": "sjflkdjsflsdj"})
        res = r.json()
        e = discord.Embed(description="""This bot is still in beta. DM `cynx#9038` if there are any problems.\n
        Fixing problem where nothing shows ASAP :)""")
        url = res['data']['children'][random.randint(0, 25)]['data']['url']
        e.set_image(url=url)
        await ctx.reply(embed=e)
