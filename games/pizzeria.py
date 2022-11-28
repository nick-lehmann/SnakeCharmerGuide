class InvalidPizzaToppingError(Exception):
    pass


class InvalidTemperatureError(Exception):
    pass


def make_pizza(topping, temperature):
    temperature = int(temperature)
    if temperature < 200:
        raise InvalidTemperatureError()

    valid_toppings = ["mushrooms", "salami"]
    if topping not in valid_toppings:
        raise InvalidPizzaToppingError(f"You monster! We don't put {topping} on pizza!")

    print(f'🍕 Your {topping} pizza is ready!')


while True:
    print('')
    topping = input("🍄 Topping: ")
    temperature = input('🔥 Temperature: ')

    try:
        make_pizza(topping, temperature)
    except InvalidTemperatureError:
        print("🚨 Temperature is too low!")
    except InvalidPizzaToppingError as e:
        print(f'🚨 {e}')
    except ValueError:
        print("🚨 Temperature must be an integer!")

    break
