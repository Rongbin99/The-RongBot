import discord 
from discord.ext import commands, tasks

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def debug(self, ctx):
        
        await ctx.send(f"")


async def setup(client):
    await client.add_cog(Test(client))
