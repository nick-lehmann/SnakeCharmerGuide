import requests

endpoint = "https://api.studentenwerk-dresden.de/openmensa/v2"

def list_canteens():
    r = requests.get(f"{endpoint}/canteens")

    canteens = r.json()
    canteens.sort(key=lambda canteen: canteen["id"])

    return canteens.json()

def get_menu(canteen: int, date: str):
    return requests.get(f"{endpoint}/canteens/{canteen}/days/{date}/meals").json()


for canteen in list_canteens():
    print(f"{canteen['id']}: {canteen['name']}")

print()
selected = int(input("Select a canteen: "))

today = "2023-01-04"
for meal in get_menu(selected, today):
    print(f"{meal['name']}: {meal['prices']['Studierende']}€")