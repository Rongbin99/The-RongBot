import requests
from discord.ext import commands, tasks
from kokonuts import ticketmaster_api_key
from lxml import html
from bs4 import BeautifulSoup

class aespa(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['nn'], help='aespa Toronto 2025')
    async def aespa(self, ctx):
        link = "https://www.ticketmaster.ca/202425-aespa-live-tour-synk-parallel-toronto-ontario-02-13-2025/event/10006134CABA6DDE"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive'
        }

        data = BeautifulSoup(requests.get(link, headers=headers).text)
        #data = html.fromstring(response.content)
        #prices = data.xpath('//button[@class="sc-aann0f-1 sc-1yxtdiz-0 cSILPU kcXJPS"]/text()')


        await ctx.send(data)
        print(data)
    
async def setup(client):
    await client.add_cog(aespa(client))
