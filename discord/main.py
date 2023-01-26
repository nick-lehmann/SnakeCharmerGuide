import asyncio

import add
import config
import hello
import image
import joined
import language
import report
import text
from bot import bot


async def start():
    print(f'Bot is listening for commands with prefix {await bot.get_prefix(None)}') # type: ignore


asyncio.run(start())

bot.run(config.TOKEN)