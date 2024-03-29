# Bot

## First steps

1. Create a [Discord](https://discord.com/) account if you don't have one already

2. Join [our server here](https://discord.gg/pKXkZRHn4C) or create your own server.

## Creating your first Bot

1. Go to the developer portal [discord.com/developers/](https://discord.com/developers/)
2. Create an App & Bot
3. Give it a Name and Picture
4. Got to the _Bot_ tab and create a new bot
5. Click _Regenerate Token_ and copy id. This will be your `TOKEN`.
6. Under _Privileged Gateway Intents_ enable _Message Content Intent_ and save the settings.
7. Add the Bot
8. Go to the _OAuth2_ -> _URL Generator_
9. Select _bot_ and _applications.commands_
10. Under _bot permissions_ select _Administrator_
11. Copy the url at the bottom
12. Open the url in the browser and add it to the server of your choice.
13. Get your `GUILD` id.
14. Go to settings, advanced, and turn on developer mode.
15. In the sidebar, where the servers are listed, right click the server and click _Copy ID_. This will be our `GUILD`.

#### Running the Bot

First we will install the `py-cord` library, which will help us creating a bot.

```bash
python3 -m install py-cord
```

Now you can run the minimal bot possible:

```python
import discord
from discord.ext import commands

TOKEN = 'my token'
GUILD = 'guild id'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.slash_command(guild_ids=[GUILD])
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond('Pong')

bot.run(TOKEN)
```

Add your `TOKEN` and `GUILD` in the script, then run.

```bash
python main.py
```

## Tasks

The idea is that you can on your own implement different features for the discord bot. All using the [Pycord](https://docs.pycord.dev/en/stable/) library.

We have provided a few examples, but you can also thing of your own tasks of course.

There is no particular order in which to do them, just pick the one you are more confortable with and start.

### Add Command

| Difficoulty | External Modules |
| ----------- | ---------------- |
| 1           | None             |

The goal here is add a so called "Slash Command" `/add` to your bot, in order to add two numbers together. So if you would send `/add 1 2` to the server, it would reply with `3`.

### Image search

| Difficoulty | External Modules |
| ----------- | ---------------- |
| 3           | `requests`or `aiohttp` |

The goal is to have a bot which can send pictures of a random search query you specify. So if you send `/image car` it would post a random picture of a car in reply to your command.

Therefore, we have provided you with a simple service at `https://pexels.cupcakearmy.workers.dev/<query>` where you replace `<query>` with a `car` for example. It will return multiple random URLs to images that match your query. It's not perfect, if it doesn't work, try another query.

### Joined

| Difficoulty | External Modules |
| ----------- | ---------------- |
| 2           | None             |

We want to have a command that shows when a user joined the server. This should be possible in 2 ways.

1. With a slash command `/joined` -> shows your own join date.
2. With a slash command `/joined <username>` -> shows the join date of `<username>`.
3. Right click on a username -> in the context menu -> apps -> show join date.

### Language Detection

| Difficoulty | External Modules          |
| ----------- | ------------------------- |
| 2           | `pycountry`, `langdetect` |

When you right click on a message, the bot will detect the language and return a message saying what language the message is written in. For this use the modules listed above to detect and the find the language name.



### Canteens

| Difficoulty  | External Modules          |
| ----------- | ------------------------- |
| 3           | `requests` |

Let's mensa again! Here, we will reuse our solution for the [canteens](../games/canteens.py) game but make the meal plan available via your discord bot.

Docs:
- [Sample Openmensa Meals](https://api.studentenwerk-dresden.de/openmensa/v2/canteens/6/days/2023-02-02/meals)
- [Openmensa API Docs](https://docs.openmensa.org/api/v2/canteens/)

##### Part 1 (Simple):
- Add a slash command that takes an optional `int` argument (canteen id).
- If the user does not provide the integer, the bot should return a list of all canteens alongside their associated id.
- If the user provides the id of a canteen, return the menu for the current day as a text, alongside all relevant information (especially the price). 

##### Part 2 (A little fancier):
- Make the choice of the canteen more accessible by using a select/dropdown menu
- Think about what the labels and values for each `SelectOption` should be 
- Handle the sending of the daily menu in the callback of the select

- [Example](https://github.com/Pycord-Development/pycord/blob/master/examples/views/dropdown.py)
- [Docs](https://docs.pycord.dev/en/stable/api/models.html#discord.SelectMenu)

##### Part 3 (Really fancy):
- Make the menu look nice by using a paginator with embeds for each meal
- Include all relevant information in the `Embed` (name, price, category, allergens, image)
- Tip: For some reason, setting the image URL in the `Embed` constructor does not work. Use the `.set_image()` method instead.
- Tip: If you set the image URL for the `Embed` and still get an error, have a look at the error message 😉

- [Example Paginator](https://github.com/Pycord-Development/pycord/blob/master/examples/views/paginator.py)
- [Docs Paginator](https://github.com/Pycord-Development/pycord/blob/master/examples/views/paginator.py)
- [Docs Embeds](https://docs.pycord.dev/en/stable/api/data_classes.html#embed)

In case you have too much time, you might try:
- Error handling for fetching information from the API
- Removing the original message after the user has selected a canteen