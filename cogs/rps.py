import discord
from discord.ext import commands, tasks
import random

class RPS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rps(self, ctx, input):
        if input == "rock" or "paper" or "scissors":
            oppo = random.choice(['rock', 'paper', 'scissors'])
            if oppo == input:
                await ctx.send(f"I picked {oppo}, you picked {input}. It's a tie!")
            elif oppo == 'rock' and input == 'paper':
                await ctx.send(f"I picked {oppo}, you picked {input}. You win!")
            elif oppo == 'rock' and input == 'scissors':
                await ctx.send(f"I picked {oppo}, you picked {input}. I win!")
            elif oppo == 'paper' and input == 'rock':
                await ctx.send(f"I picked {oppo}, you picked {input}. I win!")
            elif oppo == 'paper' and input == 'scissors':
                await ctx.send(f"I picked {oppo}, you picked {input}. You win!")
            elif oppo == 'scissors' and input == 'rock':
                await ctx.send(f"I picked {oppo}, you picked {input}. You win!")
            elif oppo == 'scissors' and input == 'paper':
                await ctx.send(f"I picked {oppo}, you picked {input}. I win!")
            else:
                await ctx.send(f'Whoops, please pick "rock" "paper" or "scissors"')
    @rps.error
    async def rps_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Whoops, please pick "rock" "paper" or "scissors"')

async def setup(client):
    await client.add_cog(RPS(client))
