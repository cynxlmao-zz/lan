import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        e = discord.Embed(title="Help", description="""
        `;`**helpg** • Shows general help commands
        `;`**helpa** • Shows admin help commands\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.reply(embed=e)

    @commands.command()
    async def helpg(self, ctx):
        e = discord.Embed(title="Help General", description="""
        `;`**helpg** • Shows this menu
        `;`**helpa** • Shows admin help commands
        `;`**hello OR hi** • Says hello to you
        `;`**invite** • Invites Lan to your server
        `;`**userinfo** • Shows info of mentioned user
        `;`**membercount OR mc** • Shows the amount of members in guild
        `;`**cat** • Shows a cat
        `;`**dog** • Shows a dog
        `;`**avatar OR av** • Shows avatar of mentioned user
        `;`**banner OR an** • Shows banner of mentioned user
        `;`**nobitches** • No bitches?
        `;`**meme OR memes** • Shows meme
        `;`**hydrate** • Hydrates mentioned user
        `;`**ping OR latency** • Shows ping or latency of bot\n
        **NSFW Commands** `Must be in NSFW channel`
        `;`**femboy** • Shows a femboy
        `;`**hentai** • Shows hentai
        `;`**porn OR sex** • Shows porn
        `;`**gay OR homo OR lesbian** • Shows homosexual things\n
        **More to come!**\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.
        """)
        await ctx.reply(embed=e)

    @commands.command()
    async def helpa(self, ctx):
        e = discord.Embed(title="Help Admin", description="""
        `;`**helpa** • Shows this menu
        `;`**ban OR b** • Bans mentioned user
        `;`**kick OR k** • Kicks the mentioned user
        `;`**nuke, n, OR clear** • Nukes current channel\n
        **More to come!**\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.
        """)
        await ctx.reply(embed=e)