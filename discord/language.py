import discord
import pycountry
from langdetect import detect

import config
from bot import bot


@bot.message_command(name="Detect language")
async def language(ctx: discord.ApplicationContext, message: discord.Message):
    detected = detect(message.content)
    language = pycountry.languages.get(alpha_2=detected)
    await ctx.respond(f'I think its: {language.name}')
