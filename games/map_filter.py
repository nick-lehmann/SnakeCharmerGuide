# 1
def my_filter(number):
    return number != 7


# Map & Filter
numbers = ['1', '-5', '3', '0', '-2', '-4', '7', '0', '3', '-1', '2', '8']
numbers = map(int, numbers)
numbers = map(abs, numbers)
numbers = filter(my_filter, numbers)
total = sum(numbers)
print(total)

# Comprehensions
numbers = ['1', '-5', '3', '0', '-2', '-4', '7', '0', '3', '-1', '2', '8']
numbers = [int(x) for x in numbers]
numbers = [abs(x) for x in numbers if x != 7]
total = sum(numbers)
print(total)

#

# 2
drinks = [
    {"name": "Kolle-Mate", "caffeine": 20, "price": 2.37},
    {"name": "Biozisch Mate", "caffeine": 20, "price": 2.97},
    {"name": "Muntermate", "caffeine": 20, "price": 7.65},
    {"name": "Club Mate", "caffeine": 20, "price": 1.58},
    {"name": "Flora Mate", "caffeine": 18, "price": 1.95},
    {"name": "1337", "caffeine": 29, "price": 1},
    {"name": "Maya Mate", "caffeine": 21.5, "price": 1.95},
    {"name": "Mio Mate", "caffeine": 20, "price": 1.18},
]

for mate in drinks:
    mate['power'] = mate['caffeine'] / mate['price']


def select_power(mate):
    return mate['power']


most_powerful = sorted(drinks, key=select_power, reverse=True)
print(f"Best: {most_powerful[0]['name']} \t Worst: {most_powerful[-1]['name']}")
