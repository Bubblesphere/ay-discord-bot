import praw
import discord
from discord.ext import commands

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

reddit_object = praw.Reddit(client_id = os.environ.get("REDDIT_CLIENT_ID"),
                     client_secret = os.environ.get("REDDIT_CLIENT_SECRET"),
                     user_agent = "aySH Bot")

# Verify that we are in `read_only` mode
print(reddit_object.read_only)

async def top_subreddit(subreddit, time):
    tops = reddit_object.subreddit(subreddit).top(time, limit = 1)
    for top in tops:
        await client.say(top.url)

# Bot config
prefix = '!'
des = 'aySH'
client = commands.Bot(description=des, command_prefix=prefix)

# Make a startup command
@client.event
async def on_ready():
    print("[*]I'm in")
    print('[*] Name: {}'.format(client.user.name))

# subreddit
@client.command(pass_context=True)
async def reddit(ctx, subreddit = "all", time = "day"):
    await top_subreddit(subreddit, time)

# random
@client.command(pass_context=True)
async def random(ctx):
    await top_subreddit('random', 'all')

# probuild
@client.command(pass_context=True)
async def build(ctx, champion = "janna"):
    await client.say('http://www.probuilds.net/champions/details/' + champion)

# counter
@client.command(pass_context=True)
async def counter(ctx, champion = "janna"):
    await client.say('http://lolcounter.com/champions/' + champion)

client.run(os.environ.get("DISCORD_CLIENT_TOKEN"))
