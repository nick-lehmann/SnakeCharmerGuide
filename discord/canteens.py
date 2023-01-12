from bot import bot
from discord import ApplicationContext
import requests
from typing import Any

openmensa_endpoint = "https://api.studentenwerk-dresden.de/openmensa/v2"

def list_canteens() -> list[Any]:
    r = requests.get(f"{openmensa_endpoint}/canteens")

    canteens = r.json()
    canteens.sort(key=lambda canteen: canteen["id"])

    return canteens


@bot.message_command()
async def get_canteens(ctx: ApplicationContext):
    canteens = list_canteens()
    
    await ctx.response.send_message(
        "\n".join([f"{canteen['id']}: {canteen['name']}" for canteen in canteens])
    )