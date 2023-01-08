import discord

import config
from bot import bot


@bot.slash_command(guild_ids=[config.GUILD])
async def add(ctx: discord.ApplicationContext, a: int, b: int):
    await ctx.respond(f"{a} + {b} = {a+b}")
