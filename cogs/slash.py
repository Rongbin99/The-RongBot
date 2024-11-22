import discord, random, urllib, json
from discord.ext import commands, tasks
from discord import app_commands
# from discord import Option, OptionChoice
from discord.ext.commands import has_guild_permissions
from urllib.request import Request, urlopen

class Slash(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="ping", description = "Test the latency of the bot.")
    async def ping(self, ctx):
        await ctx.respond(f'Bong!!! `{round(self.client.latency * 1000, ndigits=2)} ms` :)')

    # @commands.tree.command(description = "Check your Valorant Rank")
    # async def valorantrank(self, interaction: discord.Interaction, username: Option(str, 'Username in Game (for spaces use "_")', required = True), tag: Option(str, 'Tag (the stuff after the "#")', required = True)):
    #     response = urlopen(Request(f"https://api.kyroskoh.xyz/valorant/v1/mmr/na/{username}/{tag}",
    #     headers={
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    #     },))
    #     await interaction.respond(response.read().decode())

    # @commands.tree.command(description = "Need help with a calculation?")
    # async def calc(self, interaction: discord.Interaction, operation: Option(int, "Mathematical Operation", choices = [
    #     OptionChoice(name='Add', value=1),
    #     OptionChoice(name='Subtract', value=2),
    #     OptionChoice(name='Multiply', value=3),
    #     OptionChoice(name='Divide', value=4),
    #     ], required = True), num1: Option(float, required = True), num2: Option(float, required = True)):
    #     if operation == 1:
    #         ans = num1 + num2
    #         await interaction.respond(f"The answer is {str(ans)}")
    #     elif operation == 2:
    #         ans = num1 - num2
    #         await interaction.respond(f"The answer is {str(ans)}")
    #     elif operation == 3:
    #         ans = num1 * num2
    #         await interaction.respond(f"The answer is {str(ans)}")
    #     elif operation == 4:
    #         if num2 == 0:
    #             await interaction.respond(f"Whoops, you cannot divide by zero!")
    #         else:
    #             ans = num1 / num2      
    #             await interaction.respond(f"The answer is {str(ans)}")

    # @commands.tree.command(description = "Play Rock, Paper, Scissors.")
    # async def rps(self, interaction: discord.Interaction, input: Option(str, "Pick Rock, Paper, or Scissors", choices = [
    #     OptionChoice(name='Rock', value='rock'),
    #     OptionChoice(name='Paper', value='paper'),
    #     OptionChoice(name='Scissors', value='scissors'),
    #     ], required = True)):
    #     oppo = random.choice(['rock', 'paper', 'scissors'])
    #     if oppo == input:
    #         await interaction.respond(f"I picked {oppo}, you picked {input}. It's a tie!")
    #     elif oppo == 'rock' and input == 'paper':
    #         await interaction.respond(f"I picked {oppo}, you picked {input}. You win!")
    #     elif oppo == 'rock' and input == 'scissors':
    #         await interaction.respond(f"I picked {oppo}, you picked {input}. I win!")
    #     elif oppo == 'paper' and input == 'rock':
    #         await interaction.respond(f"I picked {oppo}, you picked {input}. I win!")
    #     elif oppo == 'paper' and input == 'scissors':
    #         await interaction.respond(f"I picked {oppo}, you picked {input}. You win!")
    #     elif oppo == 'scissors' and input == 'rock':
    #         await interaction.respond(f"I picked {oppo}, you picked {input}. You win!")
    #     elif oppo == 'scissors' and input == 'paper':
    #         await interaction.respond(f"I picked {oppo}, you picked {input}. I win!")

    @app_commands.command(description = "Resets the value of pets")
    @has_guild_permissions(administrator=True)
    async def goodreset(self, ctx):
        num = open("../storage.txt", "w")
        num.write(str(0))
        num.close()
        await ctx.send(f'Successfully resetted.')
    @goodreset.error
    async def goodreset_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You don't have the required power.")

    # @commands.tree.command(description = "Perform a unit conversion.")
    # async def ai(self, interaction: discord.Interaction, querystring: Option(str, "Insert what you wish to search", required=True)):
    #     input = querystring.replace(" ", "%20")
    #     response = urlopen(Request(f"http://api.wolframalpha.com/v2/query?appid=J9QK97-44GGG92ER3&input={input}&includepodid=Result&format=plaintext&output=json",
    #     headers={
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    #     },)).read()
    #     data = json.loads(response)
    #     await interaction.respond(data['queryresult']['pods'][0]['subpods'][0]['plaintext'])
    # @ai.error
    # async def ai_error(self, ctx, error):
    #     if isinstance(error, commands.CommandInvokeError):
    #         await ctx.send(f'Query unsuccessful or has no result.')

async def setup(client):
    await client.add_cog(Slash(client))
    
