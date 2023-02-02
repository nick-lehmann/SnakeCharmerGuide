from datetime import date
from typing import Optional
import requests
from bot import bot
import discord
from discord import ApplicationContext

ENDPOINT = "https://api.studentenwerk-dresden.de/openmensa/v2"


# ========
# Canteens
# ========
class Canteen:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.name} ({self.id})"


def canteen_from_openmensa_json(canteen: dict) -> Canteen:
    return Canteen(
        id=canteen["id"],
        name=canteen["name"]
    )

def list_canteens() -> list[Canteen]:
    r = requests.get(f"{ENDPOINT}/canteens")

    canteens = [canteen_from_openmensa_json(canteen) for canteen in r.json()]
    canteens.sort(key=lambda canteen: canteen.id)

    return canteens


# =====
# Meals
# =====
class Meal:
    name: str
    price: float

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f"{self.name} ({self.price}€)"


def meal_from_openmensa_json(meal: dict) -> Meal:
    return Meal(
        name=meal["name"],
        price=meal["prices"]["Studierende"],
    )


def list_meals(canteen_id: int, day: date) -> list[Meal]:
    day_string = day.strftime("%Y-%m-%d")
    meals = requests.get(f"{ENDPOINT}/canteens/{canteen_id}/days/{day_string}/meals").json()

    return [meal_from_openmensa_json(meal) for meal in meals]


# =======
# Discord
# =======
def canteens_to_options(canteens: list[Canteen]) -> list[discord.SelectOption]:
    return [
        discord.SelectOption(
            label=str(canteen),
            description=f"Show menu for {canteen.name}",
            value=str(canteen.id)
        )
        for canteen in canteens
    ]

class CanteenDropdown(discord.ui.Select):
    async def callback(self, interaction: discord.Interaction):
        canteen_id = int(self.values[0]) # type: ignore
        meals = list_meals(canteen_id, date.today())
        meals = map(str, meals)
        msg = "\n".join(meals)
        await interaction.response.send_message(msg)

# ========
# Commands
# ========
@bot.slash_command()
async def nick_food(ctx: ApplicationContext):
    canteens = list_canteens()
    canteen_options = canteens_to_options(canteens)
    dropdown = CanteenDropdown(options=canteen_options)
    view = discord.ui.View(dropdown)
    await ctx.respond(view=view)
