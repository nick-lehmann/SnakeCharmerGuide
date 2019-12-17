"""
You are going to implement the "Guess my number" play. When the game starts, the computer chooses a random number
from a given range (e.g. one to six, but any other will do). Then, the user has three rounds to guess the number.
After entering his or her guess, the user gets a message if the guess was too low or too high. If the guess was correct,
the game is over and he/she has won. Otherwise, the next rounds starts. If the user did not guess the number after three
rounds, he/she has lost.

NOTE: Use the [random](https://docs.python.org/3/library/random.html) package from the standard library.
BONUS: Let the user choose the range of numbers the secret number can be chosen from.
"""
import random


secret_number = random.randint(1, 6)


def play_round():
    """ Play one round of guess my number """
    user_input = int(input('What is your guess?: '))

    if user_input == secret_number:
        print('Your correct!')
        return True

    if user_input < secret_number:
        print('Too low 🔻')
        return False

    if user_input > secret_number:
        print('Too high 💨')
        return False


print('Guess my number!')
for round in range(1, 4):
    is_correct = play_round()
    if is_correct:
        break

if not is_correct:
    print('Sorry but nope 🤷🏻‍♂️')
