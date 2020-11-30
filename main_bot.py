# First attempt at a Chatbot
# Not sure what this is going to be used for.
# November 29, 2020

import discord
from discord.ext import commands

# Currently using Ctrl+Alt+M to kill this process...

# Importing key from a token.txt file, because security?
TOKEN = open("token.txt","r").readline()

client = commands.Bot(command_prefix = '!ping')
# We'll mention the prefix later

# Answers with ms latency

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms ')

client.run(TOKEN)
