import io

import aiohttp
import requests
import config
from bot import bot

from discord import ApplicationContext, File

URL = 'https://pexels.cupcakearmy.workers.dev/{query}'

async def fetch_image(query: str) -> io.BytesIO:
    session = aiohttp.ClientSession() 
    search = await session.get(URL.format(query=query))
    if search.status != 200:
        raise ValueError("Failed to search for image")
    
    url = await search.text()
    search.close()

    image = await session.get(url)
    content = io.BytesIO(await image.read())
    image.close()

    await session.close()
    return content

def fetch_image_sync(query: str) -> io.BytesIO:
    search = requests.get(URL.format(query=query))
    if search.status_code != 200:
        raise ValueError("Failed to search for image")
    url = search.text

    image = requests.get(url)
    return io.BytesIO(image.content)

@bot.slash_command(guild_ids=[config.GUILD])
async def image(ctx: ApplicationContext, query: str):
    try:
        # image = await fetch_image(query)
        image = fetch_image_sync(query)
        await ctx.respond(file=File(image, filename=f'{query}.jpg'))
    except Exception as e:
        print(e)
        await ctx.respond("Soooooooory, failed to fetch you an image...")