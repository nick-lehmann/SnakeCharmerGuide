import requests

# List all canteens
endpoint = "https://api.studentenwerk-dresden.de/openmensa/v2"
r = requests.get(f"{endpoint}/canteens")

canteens = r.json()
canteens.sort(key=lambda canteen: canteen["id"])

for canteen in canteens:
    print(f"{canteen['id']}: {canteen['name']}")

# Ask for canteen id
print()
selected = int(input("Select a canteen: "))

# Fetch todays menu
today = "2023-01-04"
r = requests.get(f"{endpoint}/canteens/{selected}/days/{today}/meals")

for meal in r.json():
    print(f"{meal['name']}: {meal['prices']['Studierende']}€")