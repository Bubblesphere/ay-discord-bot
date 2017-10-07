""" Discord Bot """

import os

import praw
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

import helper

load_dotenv(find_dotenv())

REDDIT = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent="aySH Bot")

# Verify that we are in `read_only` mode
print(REDDIT.read_only)

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
    await helper.top_subreddit(CLIENT, REDDIT, subreddit, time)


# random
@CLIENT.command(pass_context=True)
async def random(ctx):
    await helper.top_subreddit(CLIENT, REDDIT, 'random', 'all')


# probuild
@CLIENT.command(pass_context=True)
async def build(ctx, champion="janna"):
    await CLIENT.say('http://www.probuilds.net/champions/details/' + champion)


# counter
@CLIENT.command(pass_context=True)
async def counter(ctx, champion="janna"):
    await CLIENT.say('http://lolcounter.com/champions/' + champion)


@CLIENT.command(pass_context=True)
async def ben(ctx):
    await helper.play(CLIENT, await helper.get_user_voice_channel(ctx),
                      'sound/ben.mp3')


@CLIENT.command(pass_context=True)
async def yt(ctx, link):
    await helper.play_youtube(CLIENT, await helper.get_user_voice_channel(ctx),
                              link)


CLIENT.run(os.environ.get("DISCORD_CLIENT_TOKEN"))
