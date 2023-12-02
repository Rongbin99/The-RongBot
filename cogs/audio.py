import discord
from discord.ext import commands, tasks
import os
#broken
class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['p'], help='Plays audio from a source link.')
    async def play(self, ctx, url : str, channel):
        VC = discord.utils.get(ctx.guild.voice_channels, name=channel)
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        await voice.connect()
        await ctx.send(f'Successfully connected!')

    @commands.command(aliases=['dc', 'disconnect'], help='Disconnects bot from the voice channel.')
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
            await ctx.send(f'Successfully disconnected!')
        else:
            await ctx.send(f'It seems that I was always disconnected.')
    
    @commands.command(help='Pauses the currently playing audio.')
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send(f'PAUSED!')
        else:
            await ctx.send(f'How does one pause audio thats not playing?')
        
    @commands.command(aliases=['cont', 'continue'], help='Resumes the paused audio.')
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.send(f'RESUMED!')
        else:
            await ctx.send(f'How does one resume audio thats already playing?')

    @commands.command(help='Stops the currently playing audio.')
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()
        await ctx.send(f'Stopped the audio.')

def setup(client):
    client.add_cog(Audio(client))