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
    
    return number

def play_round(guess):
    """ Play one round of guess my number """
    if guess == secret_number:
        print('Your correct!')
        return True

    if guess < secret_number:
        print('Too low 🔻')
        return False

    if guess > secret_number:
        print('Too high 💨')
        return False


print('Guess my number!')
rounds = 1
found = False
start = time.time()

while True:
    try:
        guess = input('What is your guess?: ')
        guess = validate_guess(guess)
        is_correct = play_round(guess)
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