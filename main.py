import discord, os, asyncio
from kokonuts import bot_token, cogs_path
from discord.ext import commands, tasks

intents = discord.Intents.all()
#game = discord.Streaming(platform='Twitch', name="chillin' :3", game='Walnuts', url='https://www.twitch.tv/rongbin99', twitch_name='Rongbin99')
game = discord.Game('with your Walnuts')
prefix = 'r.'

client = commands.Bot(command_prefix = commands.when_mentioned_or(prefix), intents=intents, status=discord.Status.idle, activity=game, help_command=None)

@client.tree.command(name="help", description = 'Sends the help menu for this bot.')
async def help(ctx):
    em = discord.Embed(title='The RongBot™️ Help Menu', description=f'Use {prefix}help <command> for specific help with that command.\n_ _\n < > indicates the value is required\n[ ] indicates the value is optional', color=ctx.author.color)
    em.add_field(name='Moderation', value=f'kick\nban\nunban\npurge\nuserinfo\nserverinfo')
    em.add_field(name='Fun', value=f'8ball\nshoutout\nrps\ncalc\nkirby\nduck\ncoinflip')
    em.add_field(name='Audio', value=f'play\npause\nresume\nstop\nleave')
    em.add_field(name='Misc.', value=f'ping\nsay\ndm\npet\nvalrank\nai\nhelp')
    await ctx.respond(embed = em)

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title='The RongBot™️ Help Menu', description=f'Use {prefix}help <command> for specific help with that command.\n_ _\n < > indicates the value is required\n[ ] indicates the value is optional', color=ctx.author.color)
    em.add_field(name='Moderation', value=f'kick\nban\nunban\npurge\nuserinfo\nserverinfo')
    em.add_field(name='Fun', value=f'8ball\nshoutout\nrps\ncalc\nkirby\nduck\ncoinflip')
    em.add_field(name='Audio', value=f'play\npause\nresume\nstop\nleave')
    em.add_field(name='Misc.', value=f'ping\nsay\ndm\npet\nvalrank\nai\nhelp')
    await ctx.send(embed = em)
@help.command(aliases=['test'])
async def ping(ctx):
    em = discord.Embed(title='Ping', description=f'Checks the responsiveness of the RongBot™️.',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}ping')
    await ctx.send(embed=em)
@help.command(aliases=['boot'])
async def kick(ctx):
    em = discord.Embed(title='Kick', description=f'Kicks a member from the server.\n_ _\n < > indicates the value is required\n[ ] indicates the value is optional',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}kick <member> [reason]')
    await ctx.send(embed=em)
@help.command()
async def ban(ctx):
    em = discord.Embed(title='Ban', description=f'Bans a member from the server.\n_ _\n < > indicates the value is required\n[ ] indicates the value is optional',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}ban <member> [reason]')
    await ctx.send(embed=em)
@help.command()
async def unban(ctx):
    em = discord.Embed(title='Unban', description=f'Unbans a member from the server.\n_ _\n < > indicates the value is required',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}unban <member>')
    await ctx.send(embed=em)
@help.command(alises=['clear'])
async def purge(ctx):
    em = discord.Embed(title='Purge/Clear', description=f'Clears a set amount of messages from a channel.\n_ _\n < > indicates the value is required',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}purge <amount>')
    await ctx.send(embed=em)
@help.command(aliases=['8ball'])
async def _8ball(ctx):
    em = discord.Embed(title='8ball', description=f'Gives you good wisdom, mayhaps.\n_ _\n < > indicates the value is required',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}8ball <prompt>')
    await ctx.send(embed=em)
@help.command(aliases=['so'])
async def shoutout(ctx):
    em = discord.Embed(title='Shoutout', description=f'Gives a member a special shoutout!\n_ _\n < > indicates the value is required',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}shoutout <member>')
    await ctx.send(embed=em)
@help.command()
async def rps(ctx):
    em = discord.Embed(title='Rock Paper Scissors', description=f'Plays rock, paper, scissors against the bot.\n_ _\n < > indicates the value is required',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}rps <rock/paper/scissors>')
    await ctx.send(embed=em)
@help.command(aliases=['calculator'])
async def calc(ctx):
    em = discord.Embed(title='Basic Calculator', description=f'A calculator capable of performing basic operations.',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}calc')
    await ctx.send(embed=em)
@help.command()
async def say(ctx):
    em = discord.Embed(title='The Say Command', description=f'The bot repeats after you!\n_ _\n < > indicates the value is required',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}say <message>\n_ _\n{prefix}esay <message> - Makes it an embed.')
    await ctx.send(embed=em)
@help.command()
async def dm(ctx):
    em = discord.Embed(title='The DM Command', description=f'The bot DMs a user for you!\n_ _\n < > indicates the value is required\n[ ] indicates the value is optional',color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}dm <user> [message]\n_ _\n{prefix}edm <user> [message] - Makes it an embed.')
    await ctx.send(embed=em)
@help.command()
async def pet(ctx):
    em = discord.Embed(title='Pet the RongBot™️', description=f'Gives the RongBot™️ a nice pet.', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}pet')
    await ctx.send(embed=em)
@help.command()
async def userinfo(ctx):
    em = discord.Embed(title='Discord User Stats', description=f'Gives the stats of a user.\n_ _\n < > indicates the value is required', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}userinfo <user>')
    await ctx.send(embed=em)
@help.command()
async def serverinfo(ctx):
    em = discord.Embed(title='Discord Server Stats', description=f'Gives the stats of a server.\n_ _\n < > indicates the value is required', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}serverinfo <server>')
    await ctx.send(embed=em)
@help.command(aliases=['p'])
async def play(ctx):
    em = discord.Embed(title='Play Audio', description=f'Plays music from the given URL.\n_ _\n < > indicates the value is required', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}play <url> <vc>')
    await ctx.send(embed=em)
@help.command()
async def pause(ctx):
    em = discord.Embed(title='Pause Audio', description=f'Pauses the currently playing audio.', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}pause')
    await ctx.send(embed=em)
@help.command()
async def resume(ctx):
    em = discord.Embed(title='Resume Audio', description=f'Resumes the previously paused audio.', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}resume')
    await ctx.send(embed=em)
@help.command()
async def stop(ctx):
    em = discord.Embed(title='Stop Audio', description=f'Stops the audio from playing.', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}stop')
    await ctx.send(embed=em)
@help.command(aliases=['dc', 'disconnect'])
async def leave(ctx):
    em = discord.Embed(title='Disconnect Bot', description=f'Disconnects the bot from the VC', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}leave')
    await ctx.send(embed=em)
@help.command()
async def kirby(ctx):
    em = discord.Embed(title='Dancing Kirby', description=f'Summons the one and only dancing Kirby.', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}kirby')
    await ctx.send(embed=em)
@help.command()
async def duck(ctx):
    em = discord.Embed(title='DuckJAM', description=f'Summons a damming duck thats vibing', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}duck')
    await ctx.send(embed=em)
@help.command(aliases=['val'])
async def valrank(ctx):
    em = discord.Embed(title='Valorant Rank', description=f'Checks the Valorant Rank and RR of a player\n_ _\n[ ] indicates the value is optional', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}valrank [user + tag]')
    await ctx.send(embed=em)
@help.command()
async def coinflip(ctx):
    em = discord.Embed(title='Flip a Coin', description=f'Flips a coin resulting in heads or tails\n_ _\n[ ] indicates the value is optional', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}coinflip [# of times]')
    await ctx.send(embed=em)
@help.command()
async def ai(ctx):
    em = discord.Embed(title='AI Search', description=f'Search for something using the Wolframalpha AI\n_ _\n< > indicates the value is required', color=ctx.author.color)
    em.add_field(name='Usage', value=f'{prefix}ai <search input>')
    await ctx.send(embed=em)

@client.command(help='Load an extention.')
@commands.is_owner()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')
    await ctx.send(f'`{extension} has been loaded.`')

@client.command(help='Unload an extention.')
@commands.is_owner()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'`{extension} has been unloaded.`')

@client.command(help='Reload an extention.')
@commands.is_owner()
async def reload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await client.load_extension(f'cogs.{extension}')
    await ctx.send(f'`{extension} has been reloaded.`')

#############################################################

async def main():
    @client.event
    async def on_ready():
        print('The RongBot™️ is ready for operation.')

        await client.tree.sync()
        print('Slash commands synced.')

        for filename in os.listdir(cogs_path):
            if filename.endswith('.py'):
                try:
                    await client.load_extension(f'cogs.{filename[:-3]}')
                    print(f'Loaded extensions: {filename}')
                except Exception as e:
                    print(f'Failed to load extension {filename}: {e}')

    await client.start(bot_token)

if __name__ == "__main__":
    asyncio.run(main())
    