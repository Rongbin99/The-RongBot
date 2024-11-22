import discord
from discord.ext import commands, tasks

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Welcome {member} to the {member.guild} server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server :(')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required power.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please include all arguments (variables).")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command entered.")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Error 403: Forbidden")
        if isinstance(error, commands.NotOwner):
            await ctx.send("You are not my daddy.")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == 'coconut':
            await message.add_reaction('\U0001F965')    

async def setup(client):
    await client.add_cog(Events(client))
