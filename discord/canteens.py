from dataclasses import dataclass
from datetime import date
from typing import Any, Callable, Coroutine

import config
import requests
from bot import bot

import discord
from discord import ApplicationContext
from discord.ext import pages

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
        return f"{self.name}"


def canteen_from_openmensa_json(canteen: dict[str, Any]) -> Canteen:
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
    category: str
    image_url: str
    allergenes: set[str]

    def __init__(self, name: str, price: float, category: str, image_url: str, allergenes: set[str]):
        self.name = name
        self.price = price
        self.category = category
        self.image_url = image_url
        self.allergenes = allergenes
    
    def __str__(self) -> str:
        return f"{self.name} ({self.price}€)"


def remove_allergenes(s: str) -> tuple[str, list[str]]:
    parts = s.replace('),', ')').split(' ')
    name_parts, allergenes = [], []

    i = 0
    while i < len(parts): 
        part = parts[i]

        if part.startswith("("):
            if part.endswith(")"):
                allergenes += [part[1:-1]]
                i += 1
                continue

            allergenes += [part[1:]]
            i += 1

            while i < len(parts) and not parts[i].endswith(")"):
                allergenes += [parts[i]]
                i += 1

            if i < len(parts):
                allergenes += [parts[i][:-1]]
        else:
            name_parts += [part]

        i += 1

    return (" ".join(name_parts), allergenes)


def meal_from_openmensa_json(meal: dict[str, Any]) -> Meal:
    name, allergenes = remove_allergenes(meal["name"])

    return Meal(
        name=name,
        price=meal["prices"]["Studierende"],
        category=meal["category"],
        image_url='https:' + meal["image"],
        allergenes=set(allergenes)
    )


def list_meals(canteen_id: int, day: date) -> list[Meal]:
    day_string = day.strftime("%Y-%m-%d")
    meals = requests.get(f"{ENDPOINT}/canteens/{canteen_id}/days/{day_string}/meals").json()

    return [meal_from_openmensa_json(meal) for meal in meals]


# ===============
# Discord Helpers
# ===============
def canteens_to_options(canteens: list[Canteen]) -> list[discord.SelectOption]:
    return [
        discord.SelectOption(
            label=str(canteen),
            description=f"Show menu for {canteen.name}",
            value=str(canteen.id)
        )
        for canteen in canteens
    ]


def meals_to_paginator(meals: list[Meal]) -> pages.Paginator:
    embeds: list[discord.Embed] = []

    for meal in meals:
        embed = discord.Embed(
            type="image",
            title=meal.category,
            description=meal.name,
            fields=[
                discord.EmbedField("Preis", f"{meal.price}€", inline=True),
                discord.EmbedField("Allergene", ", ".join(sorted(meal.allergenes)), inline=True)
            ]
        )
        embed.set_image(url=meal.image_url)
        embeds += [embed]

    return pages.Paginator(pages=embeds) # type: ignore


class CanteenDropdown(discord.ui.Select):
    callback_handler: Callable[[discord.Interaction, list[Any]], Coroutine[None, None, None]]

    async def callback(self, interaction: discord.Interaction):
        canteen = int(self.values[0]) # type: ignore
        meals = list_meals(canteen, date.today())
        paginator = meals_to_paginator(meals)
        await paginator.respond(interaction)


# ========
# Commands
# ========
@bot.slash_command()
async def food_solution(ctx: ApplicationContext):
    canteens = list_canteens()
    canteen_options = canteens_to_options(canteens)

    dropdown = CanteenDropdown(options=canteen_options)

    view = discord.ui.View(dropdown)
    await ctx.respond("Pick a canteen", view=view)

