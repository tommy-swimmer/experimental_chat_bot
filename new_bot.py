# This bot was made with a Youtube Tutorial and Real Python Articles
# Python: Making a Discord bot
# By: Lucas

import discord
from discord.ext import commands
import random

# Currently using Ctrl+Alt+M to kill this process...

# Importing key from a token.txt file, because security?
TOKEN = open("token.txt","r").readline()

client = commands.Bot(command_prefix = '.') # Establishing the prefix
# We'll mention the prefix later

######################################## Some Commands ########################################
########################################               ########################################

# Prints Bot is ready, if successful, in terminal.
@client.event
async def on_ready():
    print('Bot is ready')

# Answers with ms latency
@client.command()
async def ping(ctx):    # Establishing the context for the prefix
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms ') # Sending Pong! and Latency in ms

@client.command()
async def gg(ctx):    # Establishing the context for the prefix as 'gg'
    await ctx.send(f'gg') # Reply with gee gee

@client.command()
async def google(ctx):
    await ctx.send("What would you like to search for?")

@client.command()
async def quote(ctx):
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

################################################################################
################################################################################

client.run(TOKEN)
