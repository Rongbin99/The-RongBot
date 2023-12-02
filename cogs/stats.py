import discord
from discord.ext import commands, tasks

class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, member : commands.UserConverter):
        em = discord.Embed(title=f"Discord User Stats", description=f"{member}'s Stats", color=ctx.author.color)
        em.add_field(name='User ID', value=f'{member.id}')
        em.add_field(name='Registered', value=f'{member.created_at}')
        await ctx.send(embed = em)
    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please state the user ID.")

    @commands.command()
    async def serverinfo(self, ctx, server : commands.GuildConverter):
        em = discord.Embed(title='Discord Server Stats', description=f"{server}'s Stats", color=ctx.author.color)
        em.add_field(name='Server ID', value=f'{server.id}')
        em.add_field(name='Registered', value=f'{server.created_at}')
        await ctx.send(embed = em)
    @serverinfo.error
    async def serverinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please state the server ID.")

def setup(client):
    client.add_cog(Stats(client))