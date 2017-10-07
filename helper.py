""" Helper functions """

CHANNEL_DICT = {
    'league-of-legends': '363801664785874944',
    'rocket-leauge': '363801757509353474',
    'chilling-boys': '363863510096281611',
    'afk-boys': '363817899997134848'
}


async def get_user_voice_channel(ctx):
    author = ctx.message.author
    voice_channel = author.voice_channel
    return voice_channel


async def top_subreddit(CLIENT, REDDIT, subreddit, time):
    tops = REDDIT.subreddit(subreddit).top(time, limit=1)
    for top in tops:
        await CLIENT.say(top.url)


VOICE_CLIENT = None


async def play(CLIENT, voice_channel, sound):
    # Add verification for sound
    global VOICE_CLIENT

    # Check if the bot is connected to a voice channel
    if VOICE_CLIENT is None:
        VOICE_CLIENT = await CLIENT.join_voice_channel(voice_channel)
    else:
        VOICE_CLIENT.move_to(voice_channel)

    player = VOICE_CLIENT.create_ffmpeg_player("sound/ben.mp3")
    player.start()
