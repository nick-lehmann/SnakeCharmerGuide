from dataclasses import dataclass
from datetime import date
from typing import Any, Callable, Coroutine, Optional

import config
import requests
from bot import bot

import discord
from discord import ApplicationContext

ENDPOINT = "https://api.studentenwerk-dresden.de/openmensa/v2"

@dataclass
class Canteen:
    id: int
    name: str

    @staticmethod
    def from_openmensa(canteen: dict[str, Any]) -> 'Canteen':
        return Canteen(
            id=canteen["id"],
            name=canteen["name"]
        )
    
    def __str__(self) -> str:
        return f"{self.name} ({self.id})"

@dataclass
class Meal:
    name: str
    price: float

    @staticmethod
    def from_openmensa(meal: dict[str, Any]) -> 'Meal':
        return Meal(
            name=meal["name"],
            price=meal["prices"]["Studierende"]
        )
    
    def __str__(self) -> str:
        return f"{self.name} ({self.price}€)"

def list_canteens() -> list[Canteen]:
    r = requests.get(f"{ENDPOINT}/canteens")

    canteens = [Canteen.from_openmensa(canteen) for canteen in r.json()]
    canteens.sort(key=lambda canteen: canteen.id)

    return canteens

def list_meals(canteen: int, day: date) -> list[Meal]:
    day_string = day.strftime("%Y-%m-%d")
    meals = requests.get(f"{ENDPOINT}/canteens/{canteen}/days/{day_string}/meals").json()

    return [Meal.from_openmensa(meal) for meal in meals]


def canteens_to_options(canteens: list[Canteen]) -> list[discord.SelectOption]:
    return [
        discord.SelectOption(
            label=str(canteen),
            description=f"Show menu for {canteen.name}",
            value=str(canteen.id)
        )
        for canteen in canteens
    ]

class CallbackDropdown(discord.ui.Select):
    """ Small helper class for a dropdown. """
    callback_handler: Callable[[discord.Interaction, list[Any]], Coroutine[None, None, None]]

    def __init__(self, callback_handler: Callable[[discord.Interaction, list[Any]], Coroutine[Any, Any, None]], **kwargs):
        self.callback_handler = callback_handler
        super().__init__(**kwargs)

    async def callback(self, interaction: discord.Interaction):
        await self.callback_handler(interaction, self.values)


@bot.slash_command()
async def food2(ctx: ApplicationContext):
    canteens = list_canteens()
    canteen_options = canteens_to_options(canteens)

    async def reply_with_menu(interaction: discord.Interaction, values: list[Any]):
        canteen = int(values[0])
        meals = list_meals(canteen, date.today())
        msg = "\n".join(map(str, meals))
        await interaction.response.send_message(msg)

    dropdown = CallbackDropdown(
        callback_handler=reply_with_menu,
        options=canteen_options
    )

    view = discord.ui.View(dropdown)
    await ctx.respond("Pick a canteen", view=view)


@bot.slash_command(guild_ids=[config.GUILD])
async def food(ctx: ApplicationContext, canteen: Optional[int] = None):
    if canteen is None:
        """ Show list of canteens. """
        canteens = list_canteens()
        msg = "\n".join(map(str, canteens))
        await ctx.respond(msg)
    else:
        """ Show today's meals for canteen. """
        meals = list_meals(canteen, date.today())
        msg = "\n".join(map(str, meals))
        await ctx.respond(msg)
