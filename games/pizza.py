"""
Mario is eating a pizza.
The pizza is so tasty that every time he eats a slice he wants to say "Mhhhhhh".
Every time he eats a slice his hunger gets lowered by 1.
If he is full, he stops eating and says "I'm full 🤤"
When he is finished he says "Mamma mia! Buonissima! 😋"
Say if he is still hungry after eating all the slices

Start: Define two variables, "slices" and "hunger"
"""

slices = 8
hunger = 10

for slice in range(slices):
    if hunger == 0:
        print("I'm full 🤤")
        break
    hunger = hunger - 1
    print(f'Mhhhh 🍕 {slice + 1}')

print('Mamma mia! Buonissima! 😋👩‍🍳')

if hunger > 0:
    print(f'...but could eat {hunger} more slice/s 😍')
