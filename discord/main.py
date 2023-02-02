import asyncio
import config
from bot import bot

# Different commands for our bot
import add
import canteens
import canteen_demo
import hello
import image
import joined
import language
import report
import text


async def start():
    print(f'Bot is listening for commands with prefix {await bot.get_prefix(None)}') # type: ignore


asyncio.run(start())

bot.run(config.TOKEN)