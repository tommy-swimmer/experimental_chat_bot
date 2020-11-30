# First attempt at a Chatbot
# Not sure what this is going to be used for.
# November 29, 2020

import discord
from discord.ext import commands
import random

# Currently using Ctrl+Alt+M to kill this process...

# Importing key from a token.txt file, because security?
TOKEN = open("token.txt","r").readline()

client = commands.Bot(command_prefix = '.') # Establishing the prefix
# We'll mention the prefix later

# Answers with ms latency

@client.command()
async def ping(ctx):    # Establishing the context for the prefix
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms ') # Sending Pong! and Latency in ms

@client.command()
async def gg(ctx):    # Establishing the context for the prefix as 'gg'
    await ctx.send(f'gg') # Reply with gee gee

@client.command()
async def quote(ctx):
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

client.run(TOKEN)

# As of 11/29/20: This code works while running on a terminal of some sort.