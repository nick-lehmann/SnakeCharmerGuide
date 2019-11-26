# How far can we make it?
# Renee is driving when she realises that her tank is almost empty.
# She knows her car burns a certain amount of liters of gas every 100km.
# She also knows the distance to the next gas station.
# Will she make it or will she be stranded?

# Renee drives a Jaguar F-TYPE R that consumes 10,9 l/100km.
# The next gas station is in 420km.
# She has 40 Liters of gas left

# Arnold drives a Fiat 500 that consumes 4,9 l/100km.
# The next gas station is in 285km.
# He has 15 Liters of gas left

# Annabelle drives a Renault Espace that consumes 5,8 l/100km.
# The next gas station is in 69km.
# She has 4 Liters of gas left

# Bonus Points: Will the drivers make it if they drive slowly (+10% efficiency)?


def remaining_km(consumption, liters):
    return 100 / consumption * liters


def enough_gas(consumption, liters, next_gas_station):
    return remaining_km(consumption, liters) > next_gas_station


def will_we_make_it(name, consumption, liters, next_gas_station):
    normal = enough_gas(consumption, liters, next_gas_station)
    slow = enough_gas(consumption * 0.9, liters, next_gas_station)

    if normal:
        print(f'{name} will make it to the gas station. 🚗')
    elif slow:
        print(f'{name} can make it if they drive slowly 🐌')
    else:
        print(f'{name} will be stranded on the way there 😢')


# Using normal parameters
will_we_make_it('Renee', 10.9, 40, 420)
will_we_make_it('Arnold', 4.9, 15, 285)
will_we_make_it('Annabelle', 5.8, 4, 69)


# Using named parameters
will_we_make_it('Renee', consumption=10.9, liters=40, next_gas_station=420)
will_we_make_it('Arnold', consumption=4.9, liters=15, next_gas_station=285)
will_we_make_it('Annabelle', consumption=5.8, liters=4, next_gas_station=69)
