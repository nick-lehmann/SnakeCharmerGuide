from discord import ApplicationContext
from bot import bot

@bot.slash_command()
async def hello(interaction: ApplicationContext):
    """Says hello!"""
    user = interaction.user
    if user is None:
        return
    await interaction.response.send_message(f'Hi, {user.mention}')


# @bot.command(name="nick")
@bot.command()
async def nick_test(ctx):
    print('Test command invoked')
    await ctx.reply("Hello from nick")