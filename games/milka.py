# Milka the cow needs 10 grass to do 1 chocolate
# 2 Grass grow from 1 rain.

# 1. Define a variable called "rain" and one called "grass"
# 2. With an "if" check if there is enough grass to make a chocolate
# 3. If enough, print how many choccolates we can have, otherwise be sad

# Bonus Points: Give the cow a name and print it

cow = "Milka"

rain = 30
grass = rain * 2

if grass < 10:
    print('No Chocolate today 😭')

else:
    choccolate = int(grass / 10)
    print(f'{cow} made {choccolate} today! 🐄🍫')
