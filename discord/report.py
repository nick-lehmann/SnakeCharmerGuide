import discord
from bot import bot

# This context menu command only works on messages
@bot.message_command(name='Report to Moderators')
async def report_message(ctx: discord.ApplicationContext, message: discord.Message):
    if not ctx.guild:
        await ctx.response.send_message('Failed to send your report, you do not seem to be in a guild')
        return

    # Handle report by sending it into a log channel
    log_channel = ctx.guild.get_channel(1061611766569775185)
    if not log_channel:
        await ctx.response.send_message('Failed to send your report, as there is no channel to report to')
        return

    embed = discord.Embed(title='Reported Message')
    if message.content:
        embed.description = message.content

    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at

    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view) # type: ignore

    # We're sending this response message with ephemeral=True, so only the command executor can see it
    await ctx.response.send_message(
        f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
    )