import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['b'])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member, reason=None):
        await user.ban(reason=None)
        e = discord.Embed(title="Ban", description=f"""{user.mention} has been banned.\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.send(embed=e)

    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member, reasons=None):
        await user.kick(reason=None)
        e = discord.Embed(title="Kick", description=f"""{user.mention} has been kicked.\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.send(embed=e)

    @commands.command(aliases = ['n','clear'])
    @commands.has_permissions(administrator = True)
    async def nuke(self, ctx):
        await ctx.channel.clone()
        await ctx.channel.delete()
        channel_info = [ctx.channel.category, ctx.channel.position]
        new_channel = channel_info[0].text_channels[-1]
        await new_channel.edit(position=channel_info[1])
        e = discord.Embed(title="Nuked", description=f"""{new_channel.mention} has been nuked.\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await new_channel.send(embed=e)
        
    @ban.error
    async def ban_error(self, ctx, error):
        e = discord.Embed(title="Error", description="""You do not have the permissions to ban members.\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.send(embed=e)

    @kick.error
    async def kick_error(self, ctx, error):
        e = discord.Embed(title="Error", description="""You do not have the permissions to kick members.\n
        This bot is still in beta. DM `cynx#9038` if there are any problems.""")
        await ctx.send(embed=e)
