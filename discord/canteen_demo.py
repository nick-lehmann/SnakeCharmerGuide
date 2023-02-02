from datetime import date
from typing import Optional
import requests
from bot import bot
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



# ========
# Commands
# ========
@bot.slash_command()
async def food(ctx: ApplicationContext, canteen_id: Optional[int] = None):
    if canteen_id is None:
        canteens = list_canteens()
        canteen_names = map(str, canteens)
        msg = "\n".join(canteen_names)
        await ctx.respond(msg)
    else:
        meals = list_meals(canteen_id, date.today())
        meals = map(str, meals)
        msg = "\n".join(meals)
        await ctx.respond(msg)
