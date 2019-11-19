# How far can we make it?
# Renee is driving when she realises that her tank is almost empty.
# She knows her car burns a certain ammount of liters of gas every 100km.
# She also knows the distance to the next gas station.
# Will she make it or will she be stranded?

# Renee drives a Jaguar F-TYPE R that consumes 10,9 l/100km.
# The next gas station is in 420km.
# She has 45 Liters of gas left

# Arnold drives a Fiat 500 that consumes 4,9 l/100km.
# The next gas station is in 285km.
# He has 15 Liters of gas left

# Annabelle drives a Renault Espace that consumes 5,8 l/100km.
# The next gas station is in 69km.
# She has 5 Liters of gas left


def remaining_km(efficiency, liters):
    return 100 / efficiency * liters


def will_we_make_it(name, efficiency, liters, next_gas_station):
    enough_gas = remaining_km(efficiency, liters) > next_gas_station
    if enough_gas:
        print(f'{name} will make it to the gas station. 🚗')
    else:
        print(f'{name} will be stranded on the way there 😢')


will_we_make_it('Renee', 10.9, 45, 420)
will_we_make_it('Arnold', 4.9, 15, 285)
will_we_make_it('Annabelle', 5.8, 5, 69)

driver1 = ['Renee', 10.9, 45, 420]
driver2 = ['Arnold', 4.9, 15, 285]
driver3 = ['Annabelle', 5.8, 5, 69]



