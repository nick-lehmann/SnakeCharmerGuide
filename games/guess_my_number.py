import random
import time

MIN, MAX = 1, 6
secret_number = random.randint(MIN, MAX)


class InvalidGuess(Exception):
    pass

def validate_guess(guess):
    """ Checks if the users understands the rules. """
    number = int(guess)

    if number < MIN or number > MAX:
        raise InvalidGuess('Your guess is out of range.')

def play_round():
    """ Play one round of guess my number """
    user_input = int(input('What is your guess?: '))
    validate_guess(user_input)

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
rounds = 1
found = False
start = time.time()
for _ in range(4):
    try:
        is_correct = play_round()
        if is_correct:
            found = True
            break
        rounds += 1
    except ValueError as e:
        print('You are too dumb for this game, it says NUMBER!')
        break
    except InvalidGuess as e:
        print('INVALID: ', e)
        print('Please try again. 🙏')
        continue

if found:
    print(f'Congratulations, you won in {rounds} rounds!')
else:
    print(f'¯\_(ツ)_/¯')

end = time.time()
print(f'All of this took {end - start} seconds.')