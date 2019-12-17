"""
Implement your own secure password generator. Ask the user how long the password should be and print the generated
password. For security reasons, every character should have the same probability to end up in the password.

NOTE: Use the [string](https://docs.python.org/3/library/string.html) module to get a list of possible characters
and the [random](https://docs.python.org/3/library/random.html) module to generate the password.
NOTE: Take a look at the [`join()` method](https://docs.python.org/3/library/stdtypes.html#str.join)
"""
import string
import random


characters = \
    string.ascii_lowercase + \
    string.ascii_uppercase + \
    string.digits + \
    string.punctuation


desired_length = int(input('How long should it be? 🤷🏻‍♂️ '))

password = ''.join(random.choices(characters, k=desired_length))
print(f'Your password is =>  {password}  <= 👩🏼‍💻')
