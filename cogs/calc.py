import math
import discord
from discord.ext import commands, tasks
#partially broken
class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['calc', 'math'], help='A basic calculator.')
    async def calculator(self, ctx):
        await ctx.send("Start calculator? (Yes/No)")
        def check(boot):
            return boot.author == ctx.author and boot.channel == ctx.channel
        boot = await self.client.wait_for("message", check=str)
        start = boot.content
        if start.lower() == "yes":
            start = True
            while True:
                try:
                    await ctx.send("First number: ")                    
                    def check(num1):
                        return num1.author == ctx.author and num1.channel == ctx.channel
                    num1 = await self.client.wait_for("message", check = check)
                    await ctx.send("Second number: ")
                    def check(num2):
                        return num2.author == ctx.author and num2.channel == ctx.channel
                    num2 = await self.client.wait_for("message", check = check)
                    await ctx.send("What operation do you wish to perform? (+ for add, - for sub, x for multiply, / for div)")
                    def check(op):
                        return op.author == ctx.author and op.channel == ctx.channel
                    op = await self.client.wait_for("message", check = check)
                    operation = op.content; val1 = num1.content; val2 = num2.content

                    if operation == "+":
                        ans = val1 + val2
                        await ctx.send(f"The answer is {round(str(ans), ndigits=3)}")
                        break

                    elif operation == "-":
                        ans = val1 - val2
                        await ctx.send(f"The answer is {round(str(ans), ndigits=3)}")
                        break

                    elif operation == "x":
                        ans = val1 * val2
                        await ctx.send(f"The answer is {round(str(ans), ndigits=3)}")
                        break

                    elif operation == "/":
                        ans = val1 / val2
                        await ctx.send(f"The answer is {round(str(ans), ndigits=3)}")
                        break

                    else:
                        await ctx.send("Invalid operation.")
                        continue

                except ValueError:
                    await ctx.send("Invalid input, try again.")
                    continue

                except ZeroDivisionError:
                    await ctx.send("Cannot divide by 0.")
                    continue

                except:
                    await ctx.send("Something went wrong.")
                    break
        else:
            start = False
            await ctx.send(f'Okay, calculator will not start.')

def setup(client):
    client.add_cog(Calculator(client))
