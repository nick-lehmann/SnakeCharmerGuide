# Reverse -> Does it make a difference if you reverse the fishes?
# Pop -> What happens if you remove the youngest fish at the beginning?
# Set -> Each fish should have a unique age at the start.


# Naive
# fishes = [3, 4, 3, 1, 2]
# new_fishes = []

# days = 80

# for day in range(days):
#     for fish in fishes:
#         if fish == 0:
#             new_fishes.append(6)
#             new_fishes.append(8)
#         else:
#             new_fishes.append(fish - 1)

#     print(f"Fishes after {day} days: {new_fishes}")
#     fishes = new_fishes
#     new_fishes = []

# print(f"After {days} days, there are {len(fishes)} fishes")


# In-Place
# fishes = [3, 4, 3, 1, 2]
# new_fishes = 0

# days = 5

# for day in range(days):
#     for i, fish in enumerate(fishes):
#         if fish == 0:
#             new_fishes += 1
#             fishes[i] = 6
#         else:
#             fishes[i] -= 1

#     fishes += new_fishes * [8]
#     new_fishes = 0
#     print(f"Fishes after {day} days: {fishes}")

# print(f"After {days} days, there are {len(fishes)} fishes")


# Keeping counts
fishes = [3, 4, 3, 1, 2]
ages = [fishes.count(i) for i in range(9)]

days = 80

for day in range(days):
    new_ages = [0] * 9
    for age, count in enumerate(ages):
        if age == 0:
            new_ages[6] += count
            new_ages[8] += count
        else:
            new_ages[age - 1] += count
    ages = new_ages


print(f"After {days} days, there are {sum(ages)} fishes")
