from discord import Interaction
from bot import client

@client.tree.command()
async def hello(interaction: Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

