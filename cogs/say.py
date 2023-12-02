import discord
from discord.ext import commands, tasks

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, message='_ _'):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{message}')

    @commands.command()
    async def esay(self, ctx, *, message='_ _'):
        await ctx.channel.purge(limit=1)
        await ctx.send(embed = discord.Embed(description=f'{message}', color=ctx.author.color))

def setup(client):
    client.add_cog(Say(client))
