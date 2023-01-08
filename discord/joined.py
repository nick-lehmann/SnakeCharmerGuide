import discord

import config
from bot import bot


async def joined_fn(ctx: discord.ApplicationContext, member: discord.Member | None = None):
    user = member or ctx.author
    date = user.joined_at
    if not date:
        await ctx.respond('Could not find that information')
    else:
        await ctx.respond(f"{user.name} joined at {discord.utils.format_dt(date)}")


@bot.slash_command(guild_ids=[config.GUILD])
async def joined(ctx: discord.ApplicationContext, member: discord.Member | None = None):
    user = member or ctx.author
    await joined_fn(ctx, user)


@bot.user_command(name="Say join date")
async def joined_menu(ctx, user: discord.Member):
    await joined_fn(ctx, user)
