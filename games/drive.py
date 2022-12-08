class AgeError(Exception):
    pass


def drive(age):
    age = int(age)
    if age < 18:
        raise AgeError("young")
    if age > 80:
        raise AgeError("old")
    print('Brumm brumm')


while True:
    try:
        age = input('What is your age? ')
        drive(age)
        break
    except ValueError:
        print('Age must be a number. Try again.')
    except AgeError as e:
        print(f'You are too {e} to drive!')
        break
