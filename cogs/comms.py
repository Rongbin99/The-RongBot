import discord
import random
import os
from discord.ext import commands, tasks
from discord.ext.commands import has_guild_permissions
from main import prefix

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['test', 'latency'], help='Test the latency of the bot.')
    async def ping(self, ctx):
        await ctx.send(f'Bong!!! `{round(self.client.latency * 1000, ndigits=2)} ms` :)')

    @commands.command(aliases=['8ball', 'magicball', 'crystalball', 'rng'], help='Would you like some wisdom?')
    async def _8ball(self, ctx, *, question):
        response = random.choice(open("V:\Walnuts\CodingFiles\Python\The RongBot\options.txt").readlines())
        await ctx.send(f'__Received:__ *{question}*\n_ _\n__The Walnut says:__ {response}')

    @commands.command(aliases=['so'], help='Gives someone a shoutout!')
    async def shoutout(self, ctx, member : commands.MemberConverter):
        await ctx.send(f'Woah who knew {member.mention} is such a cool person!')

    @commands.command(aliases=['clear', 'delete', 'del'], help='Clears a set number of messages.')
    @has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, *, amount):
        await ctx.send(f'`Deleting...`')
        await ctx.channel.purge(limit=int(amount)+2)

    @commands.command(aliases=['boot'], help='Kicks someone from the server.')
    @has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member : commands.MemberConverter, *, why='No reason given.'):
        await member.kick(reason=why)
        await ctx.send(f'**{member}** has been kicked. Reason: *{why}*')
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f'Sorry, they are too powerful for me.')
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f"Does that person exist?")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please state the user ID.")

    @commands.command(help='Bans someone from the server.')
    @has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : commands.MemberConverter, *, why='No reason given.'):
        await member.ban(reason=why)
        await ctx.send(f'**{member}** has been banned. Reason: *{why}*')
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f'Sorry, they are too powerful for me.')
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f"Does that person exist?")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please state the user ID.")

    @commands.command(help='Unbans someone from the server.')
    @has_guild_permissions(ban_members=True)
    async def unban(self, ctx, *, member : discord.User):
        await ctx.guild.unban(member)
        await ctx.send(f'**{member}** has been unbanned.')
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f"Sorry, that user couldn't be found or they've already been unbanned.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please state the user ID.")
    
    @commands.command(help='Good Walnut Bot', aliases=['pet'])
    async def good(self, ctx):
        emoji = '🥰'
        num = open("../storage.txt", "r")
        number = int(num.read())+1
        await ctx.send(f'Walnut has been petted {number} times! {emoji}')
        num.close()
        num = open("../storage.txt", "w")
        num.write(str(number))
        num.close()
    @commands.command(aliases=['petreset'])
    @has_guild_permissions(administrator=True)
    async def goodreset(self, ctx):
        num = open("../storage.txt", "w")
        num.write(str(0))
        num.close()
        await ctx.send(f'Successfully resetted.')
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == f'{prefix}pet':
            await message.add_reaction('\U0001F970')        
        if message.content == f'{prefix}good':
            await message.add_reaction('\U0001F970')
    
    @commands.command(help='Dancing Kirby goes BRRRRRR')
    async def kirby(self, ctx):
        url = 'https://cdn.discordapp.com/attachments/930901396453224539/1002671071658512474/output.webm?size=10000'
        await ctx.send(f'{url}')

    @commands.command()
    async def dkirby(self, ctx):
        url = 'https://cdn.discordapp.com/attachments/930901396453224539/1002671071658512474/output.webm?size=10000'
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{url}')

    @commands.command(help='DuckJAM goes BRRRRRR')
    async def duck(self, ctx):
        url = 'https://media.discordapp.net/attachments/459907934189649923/879171392539611136/SmartSelect_20210822-211309_Discord.gif'
        await ctx.send(f'{url}')

    @commands.command()
    async def dduck(self, ctx):
        url = 'https://media.discordapp.net/attachments/459907934189649923/879171392539611136/SmartSelect_20210822-211309_Discord.gif'
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{url}')

    @commands.command(help='Flips a coin')
    async def coinflip(self, ctx, number=1):
        number1 = number
        while number > 0:
            number = number - 1; heads = 0; tails = 0
            response = random.choice(["Heads", "Tails"])
            await ctx.send(f'The coin landed on {response}')
            if response == "Heads":
                heads = heads + 1
                continue
            elif response == "Tails":
                tails = tails + 1
                continue
            else:
                await ctx.send(f'The coin malfunctioned. Something went wrong :/')
                print(f'Something went wrong in the coinflip')
                break
        else:
            if number1 > 1:
                await ctx.send(f'Total Heads: {heads} \nTotal Tails: {tails}')

async def setup(client):
    await client.add_cog(Commands(client))
