#made this while eating a curry

#works best on freeBSD, if you use anything else you should honestly just end it


import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Ready to sext minors')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Oiling the pogostick"))

@client.command()
async def weed(ctx):
    print("with yo mommas tiddy")
    await ctx.send("sex")

@client.command()
async def sex(ctx):
    print("fuck sister")
    await ctx.send('weed')

client.run("ENTER TOKEN HERE")
