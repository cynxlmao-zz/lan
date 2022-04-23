import discord
import pytz
import requests
import random
import time
from datetime import datetime
from discord.ext import commands

class NormalCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    global startTime
    startTime = time.time()

    @commands.command(aliases=['hi'])
    async def hello(self, ctx):
        e = discord.Embed(title=f"Hello, {ctx.author}!", description="This bot is still in beta. DM `cynx#9038` if there are any problems.")
        await ctx.reply(embed=e)

    @commands.command()
    async def invite(self, ctx):
        e = discord.Embed(title="Invite Lan", url="https://discord.com/api/oauth2/authorizeclient_id=945744067399139350&permissions=8&scope=bot%20applications.commands", description="This bot is still in beta. DM `cynx#9038` if there are any problems.")
        await ctx.send(embed=e)

    @commands.command()
    async def userinfo(self, ctx, user: discord.Member):
        e = discord.Embed(title="Info", description=f"""
        {user.mention}
        ID : {user.id}
        Created on : {user.created_at:%Y-%m-%d %H:%M}
        Joined on : {user.joined_at:%Y-%m-%d %H:%M}
        Top role : {user.top_role}\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)

    @commands.command(aliases=['mc'])
    async def membercount(self, ctx):
        total = ctx.guild.member_count
        e = discord.Embed(title="Members", description=f"""There are {total} members.\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cat(self, ctx):
        r = requests.get("https://www.reddit.com/r/cat/new.json?sort=hot", headers={"User-Agent": "sjflkdjsflsdj"})
        res = r.json()
        e = discord.Embed(description="""This bot is still in beta. DM `cynx#9038` if there are any problems.
		Fixing problem where nothing shows ASAP :)""")
        url = res['data']['children'][random.randint(0, 25)]['data']['url']
        e.set_image(url=url)
        await ctx.reply(embed=e)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def dog(self, ctx):
        r = requests.get("https://dog.ceo/api/breeds/image/random").json()['message']
        e = discord.Embed(description="This bot is still in beta. DM `cynx#9038` if there are any problems.")
        e.set_image(url=r)
        await ctx.reply(embed=e)

    @commands.command(aliases=['av','pfp'])
    async def avatar(self, ctx, user: discord.Member):
        avatar = user.avatar
        e = discord.Embed(title="Avatar", description=f"""{user.mention}\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        e.set_image(url=avatar)
        await ctx.reply(embed=e)

    @commands.command(aliases=['bn'])
    async def banner(self, ctx, member: discord.Member):
        user = await self.bot.fetch_user(member.id)
        banner = user.banner.url
        e = discord.Embed(title="Banner", description=f"""{member.mention}\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        e.set_image(url=banner)
        await ctx.reply(embed=e)

    @commands.command()
    async def nobitches(self, ctx):
        e = discord.Embed(description="This bot is still in beta. DM `cynx#9038` if there are any problems.")
        e.set_image(url="https://i.redd.it/3ubd1oud7oa81.jpg")
        await ctx.reply(embed=e)

    @commands.command(aliases=['memes'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def meme(self, ctx):
        r = requests.get("https://www.reddit.com/r/memes/new.json?sort=hot", headers={"User-Agent": "sjflkdjsflsdj"})
        res = r.json()
        e = discord.Embed(description="""This bot is still in beta. DM `cynx#9038` if there are any problems.
		Fixing problem where nothing shows ASAP :)""")
        url = res['data']['children'][random.randint(0, 25)]['data']['url']
        e.set_image(url=url)
        await ctx.reply(embed=e)

    @commands.command()
    async def hydrate(self, ctx, user: discord.Member):
        e = discord.Embed(title="Hydrate", description=f"""{user.mention} has been hydrated!\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)

    @commands.command(aliases=['latency'])
    async def ping(self, ctx: commands.Context):
        e = discord.Embed(title="Ping / Latency", description=f"""{round(self.bot.latency * 1000)} ms\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)
        