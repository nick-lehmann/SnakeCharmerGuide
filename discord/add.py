from discord import ApplicationContext
from config import GUILD

from bot import bot


@bot.slash_command(guild_ids=[GUILD])
async def add(ctx: ApplicationContext, a: int, b: int):
    await ctx.respond(f"{a} + {b} = {a+b}")
