"""
The wall has been breached and cobras are attacking the castle 🏰
We see that there are 50 cobras approaching 🐍
Fortunately we have special ninjas that can defeat the cobras 🥷
Every ninja can defeat 3 cobras.
Can we defeat all the cobras with the ninjas we have?

1. Define a variable "ninjas" and one "cobras" and print if we win or loose based on the variables

Bonus Points: Say how many more ninjas do we need to win the fight!
"""

cobras = 50
ninjas = 20

if ninjas * 3 < cobras:
    print('The cobras won 🐍')

    # Bonus
    remaining_cobras = cobras - ninjas * 3
    more_ninjas_needed = remaining_cobras / 3
    print(f'We need {more_ninjas_needed} more ninjas to win the fight')
else:
    print('The ninjas won 🥷')
