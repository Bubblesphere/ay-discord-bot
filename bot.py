''' Discord Bot '''

import os

import praw
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from random import randint, choice

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
    '''Fetches the top post from a subreddit'''
    await helper.top_subreddit(CLIENT, REDDIT, subreddit, time)


# random
@CLIENT.command(pass_context=True)
async def random(ctx):
    '''Fetches the all time top post from a random subreddit'''
    await helper.top_subreddit(CLIENT, REDDIT, 'random', 'all')


# probuild
@CLIENT.command(pass_context=True)
async def build(ctx, champion="janna"):
    '''Provides a link to a League of Legends champion build'''
    await CLIENT.say('http://www.probuilds.net/champions/details/' + champion)


# counter
@CLIENT.command(pass_context=True)
async def counter(ctx, champion="janna"):
    '''Provides a link to a Leauge of Legends champion counters'''
    await CLIENT.say('http://lolcounter.com/champions/' + champion)


@CLIENT.command(pass_context=True)
async def ben(ctx):
    '''Ben says 'Queue pop!'''
    await helper.play(CLIENT, await helper.get_user_voice_channel(ctx),
                      'sound/ben.mp3')


@CLIENT.command(pass_context=True)
async def yt(ctx, link, volume = 5):
    '''Plays a youtube clip audio (good for songs)'''
    await helper.play_youtube(CLIENT, await helper.get_user_voice_channel(ctx),
                              link, volume)


@CLIENT.command(pass_context=True)
async def roll(ctx, maximum = 100):
    '''Rolls between 0-100'''
    await CLIENT.say(randint(0, maximum))


@CLIENT.command(pass_context=True)
async def drop(ctx):
    '''Randomly prints a place to drop in Fortnite'''
    places = ['Dusty Divot',
              'Fatal Fields',
              'Flush Factory',
              'Greasy Grove',
              'Haunted Hills',
              'Junk Junction',
              'Lazy Links',
              'Lonely Lodge',
              'Loot Lake',
              'Lucky Landing',
              'Paradise Palms',
              'Pleasant Park',
              'Retail Row',
              'Risky Reels',
              'Salty Springs',
              'Shifty Shafts',
              'Snobby Shores',
              'Tilted Towers',
              'Tomato Town',
              'Wailing Woods']
    await CLIENT.say(choice(places))


CLIENT.run(os.environ.get("DISCORD_CLIENT_TOKEN"))
