"""
### 🐟 Lanternfish

> This is game is from [Advent of Code 2021 Day 6](https://adventofcode.com/2021/day/6)

We are diving in the ocean when we notice a swarm of Lanterfishes. After observing a while you notice that every 7 days a Lanternfish reproduces and creates a new Lanterfish. The Lanternfish needs 2 days before it can start creating children.

We can assume that every Lanternfish has an internal clock that counts down 1 each day.

**Rules**

- When the counter reaches 0, it resets to 6 and creates a new Lanternfish with an internal counter of 8
- Otherwise, just count down by 1

Now we want to track a swarm of Lanternfishes. To do so we have a list of fish with their internal clocks.

**Example**

Starting with 5 Lanternfishes with an internal clock of 3, 4, 3, 1 and 2.
After 10 days the swarm counts 12 fish.

```
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
```

How big is the swarm after 80 days?

There are a few more things we would like to check here:

- Does it make a difference if you reverse the fish at the beginning? Check it 👍🏻
- How does the number of fish after 80 days changes, when you remove the first of the initial fish?
- Each fish should have a unique internal clock, so remove the duplicates. How does the number change?

Bonus: How big is the swarm after 256 days? (Your solution should not take more than a second)
"""

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
