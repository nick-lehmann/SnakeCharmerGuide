"""
Milka the cow needs 10 grass to create 1 chocolate bar
1 rain can give 2,5 grass

1. Define a variable called "rain" and one called "grass"
2. With an "if" check if there is enough grass to make a chocolate bar
3. If enough, print how many chocolates bar we can create, otherwise be sad

Bonus Points: Give the cow a name and print it
"""

cow = "Milka"

rain = 30
grass = rain * 2.5

if grass < 10:
    print('No Chocolate today 😭')

else:
    chocolate = int(grass / 10)
    print(f'{cow} made {chocolate} chocolate bars today! 🐄🍫')
