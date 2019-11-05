"""
You want to play rock-paper-scissors against the computer.

1. Define a dictionary for each player that stores its name and current score.
2. Ask the player about his or her name and ask how many round should be played.
3. Each round, ask the player for his or her choice. The computer should pick a random choice.
4. Evaluate each round and print who has won.

Bonus Points: Accept different spelling of each choice ('rock', 'Rock', 'rOcK') and maybe even abbreviations.
"""
from random import choice

options = ['rock', 'paper', 'scissor']

user_name = input('What is your name?: ')
number_of_rounds = int(input('How many rounds do you want to play?: '))

user_score = 0
computer_score = 0

for index in range(1, number_of_rounds + 1):
    print('==========')
    print(f'Round {index}')

    user_choice = None

    while not user_choice:
        raw = input('What is your choice?: ')
        if not raw.lower() in options:
            print('Invalid choice')
        else:
            user_choice = raw.lower()

    computer_choice = choice(options)
    print(f'The computer has chosen {computer_choice}')

    if user_choice == computer_choice:
        print('Draw! Nobody wins..')
        continue

    # User option is always the first element
    options_where_user_wins = [
        ['rock', 'scissor'],
        ['scissor', 'paper'],
        ['paper', 'rock']
    ]

    if [user_choice, computer_choice] in options_where_user_wins:
        user_score += 1
        print(f'{user_name} has won!')
    else:
        print(f'The computer has won!')
        computer_score += 1

print('----------------------')
print(f'User: {user_score} -- Computer: {computer_score}')
if user_score > computer_score:
    print(f'{user_name} has won')
elif user_score < computer_score:
    print('Computer has won')
else:
    print('It was a draw')
