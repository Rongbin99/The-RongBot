import urllib
from urllib.request import Request, urlopen
import discord 
from discord.ext import commands, tasks

class ValorantRank(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['val'], help='Check your Valorant Rank + RR')
    async def valrank(self, ctx, *, user):
        name, tag = user.split('#')
        response = urlopen(Request(f"https://api.kyroskoh.xyz/valorant/v1/mmr/na/{name}/{tag}", 
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            },))
        await ctx.send(response.read().decode())

    @valrank.error
    async def valrank_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'What is the username?')
            def check (name):
                return name.author == ctx.author and name.channel == ctx.channel
            name = await self.client.wait_for('message', check=check)
            await ctx.send(f'What is the tag?')
            def check (tag):
                return tag.author == ctx.author and tag.channel == ctx.channel
            tag = await self.client.wait_for('message', check=check)
            
            response = urlopen(Request(f"https://api.kyroskoh.xyz/valorant/v1/mmr/na/{name.content}/{tag.content}",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            },))
            await ctx.send(response.read().decode()) 




def setup(client):
    client.add_cog(ValorantRank(client))
