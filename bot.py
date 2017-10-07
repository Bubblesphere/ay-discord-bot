""" Discord Bot """

import os
import praw
from discord.ext import commands

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

REDDIT = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent="aySH Bot")

# Verify that we are in `read_only` mode
print(REDDIT.read_only)


async def top_subreddit(subreddit, time):
    tops = REDDIT.subreddit(subreddit).top(time, limit=1)
    for top in tops:
        await CLIENT.say(top.url)


# Bot config
PREFIX = '!'
DESC = 'aySH'
CLIENT = commands.Bot(description=DESC, command_prefix=PREFIX)


# Make a startup command
@CLIENT.event
async def on_ready():
    print("[*]I'm in")
    print('[*] Name: {}'.format(CLIENT.user.name))


# subreddit
@CLIENT.command(pass_context=True)
async def reddit(ctx, subreddit="all", time="day"):
    await top_subreddit(subreddit, time)


# random
@CLIENT.command(pass_context=True)
async def random(ctx):
    await top_subreddit('random', 'all')


# probuild
@CLIENT.command(pass_context=True)
async def build(ctx, champion="janna"):
    await CLIENT.say('http://www.probuilds.net/champions/details/' + champion)


# counter
@CLIENT.command(pass_context=True)
async def counter(ctx, champion="janna"):
    await CLIENT.say('http://lolcounter.com/champions/' + champion)


CLIENT.run(os.environ.get("DISCORD_CLIENT_TOKEN"))
