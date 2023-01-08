import io

import aiohttp
import config
from bot import bot

import discord


@bot.slash_command(guild_ids=[config.GUILD])
async def image(ctx: discord.ApplicationContext, query: str):
    async with aiohttp.ClientSession() as session:
        # Get image URL
        async with session.get(f'https://pexels.cupcakearmy.workers.dev/{query}') as resp:
            if resp.status != 200:
                return await ctx.respond('Could not find an image for that')
            url = await resp.text()
        # Get the actual image
        async with session.get(url) as resp:
            print(resp.status)
            data = io.BytesIO(await resp.read())
        # Reply
        await ctx.respond(file=discord.File(data, filename=f'{query}.jpg'))
