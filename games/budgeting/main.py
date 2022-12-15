import json

people = json.load(open('./people.json'))
foods = json.load(open('./food.json'))

for person in people:
    calories = 0
    price = 0
    for food in person['eats']:
        dish = foods[food]
        price += dish['price']
        calories += int(dish['kcal'])
    print(f"{person['name']} has eaten {calories}kcal and paid {price}.")
