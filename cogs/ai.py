import urllib, discord, requests, json
from discord.ext import commands, tasks
from urllib.request import Request, urlopen
from secrets_1 import  appid

class AI(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(help='Perform a unit conversion.')
    async def ai(self, ctx, *, querystring):
        input = querystring.replace(" ", "%20")
<<<<<<< HEAD
        response = urlopen(Request(f"http://api.wolframalpha.com/v2/query?appid={appid}&input={input}&includepodid=Result&format=plaintext&output=json",
=======
        response = urlopen(Request(f"http://api.wolframalpha.com/v2/query?appid=[redacted]&input={input}&includepodid=Result&format=plaintext&output=json",
>>>>>>> 685dd8c478c0a3c6746b9629c791af37daff6878
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
        },)).read()
        data = json.loads(response)
        await ctx.send(data['queryresult']['pods'][0]['subpods'][0]['plaintext'])
    @ai.error
    async def ai_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f'Query unsuccessful or has no result.')

def setup(client):
    client.add_cog(AI(client))
