# AY Discord Bot
A discord bot with the mission to fulfill needs of League enthusiasts
# Prerequisites
You need `pipenv` in order to run the bot you can find the installation instruction [here](https://github.com/kennethreitz/pipenv).

# Running the Bot
- Run `pipenv install` to install the dependancies
- Run `cp .env.sample .env` to begin setting up your environment variables
- [Setup reddit application](https://www.reddit.com/prefs/apps)
- [Setup discord token and bot](https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord)
- Add your keys to `.env`
- Then run `pipenv run python bot.py` to launch the bot

# Commands
## reddit
### Description
fetches the top post from a subreddit.
### Syntax
`!reddit [subreddit] [time]`

| Parameters | Description | Optional? | Default |
| ------ | ------ | :------: | :------: |
| subreddit | String corresponding an existing subreddit to fetch the information from | X | all |
| time | hour, day, month, year, all | X | day |

---
## random
### Description
fetches the all time top post from a random subreddit.
### Syntax
`!random`

---
## build
### Description
Provides a link to a League of Legends champion build
### Syntax
`!build [champion]`

| Parameters | Description | Optional? | Default |
| ------ | ------ | :------: | :------: |
| champion | String corresponding to a League of Legends champion. Neglect spaces and syntax | X | janna |

---
## counter
### Description
Provides a link to a League of Legends champion counters
### Syntax
`!counter [champion]`

| Parameters | Description | Optional? | Default |
| ------ | ------ | :------: | :------: |
| champion | String corresponding to a League of Legends champion. Neglect spaces and syntax | X | janna |
