import discord
from discord.ext import commands, tasks

class DM(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dm(self, ctx, user : commands.UserConverter, *, message="Hello! The person who instructed me to send you this message didn't specify what they wanted to say, so I'm going to hope that you have a wonderful day!"):
        await user.send(message)
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Successfully sent!')
    @commands.command()
    async def edm(self, ctx, user : commands.UserConverter, *, message="Hello! The person who instructed me to send you this message didn't specify what they wanted to say, so I'm going to hope that you have a wonderful day!"):
        await user.send(embed = discord.Embed(description=f'{message}', color=ctx.author.color))
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Successfully sent!')
    @dm.error
    async def dm_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f'Wow how mean. They denied your message.\n||Ensure they have the *"allow direct messages from server members"* privacy setting **on**.||')
    @edm.error
    async def edm_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f'Wow how mean. They denied your message.\n||Ensure they have the *"allow direct messages from server members"* privacy setting **on**.||')

async def setup(client):
    await client.add_cog(DM(client))
