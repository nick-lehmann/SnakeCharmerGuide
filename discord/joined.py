import discord
from datetime import datetime

import config
from bot import bot


async def joined_fn(ctx: discord.ApplicationContext, member: discord.Member):
    date = member.joined_at
    if not date:
        await ctx.respond('Could not find that information')
        return

    await ctx.respond(f"{member.name} joined at {datetime.strftime(date, '%d.%m.%Y %H:%M:%S')}")


@bot.slash_command(guild_ids=[config.GUILD])
async def joined(ctx: discord.ApplicationContext, member: discord.Member | None = None):
    user = member or ctx.author
    if not user:
        await ctx.respond("Could not find the person you are looking for")
        return
    
    if not isinstance(user, discord.Member):
        await ctx.respond("The user is not a member")
        return

    await joined_fn(ctx, user)


@bot.user_command(name="Say join date")
async def joined_menu(ctx, user: discord.Member):
    await joined_fn(ctx, user)
