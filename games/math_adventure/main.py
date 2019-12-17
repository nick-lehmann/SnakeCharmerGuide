"""
You're going to implement a few basic math methods yourself.

The goal is simple: Print a list as bullet points (each item has a dash "-" in front) and then both the
sum and the maximum of the list. The function for outputting a list as bullet points should be in its own
module and the `sum()` and `max()` function should be in their own module as well.

Tasks:
1) Add three files/modules: one for the output function, one for the math functions and one where you write your code that uses
the other two modules (e.g. `main.py`).
2) Think of a list of integers. What is its maximum element and its sum?
3) Write the output function that prints a list as bullet points.
4) Write the `max()` function that finds the maximum of the given list.
5) Write the `sum()` function that finds the sum of the given list.
"""
from abacus import sum, max
from output import print_list

l = [3, 2, 5, 4, 8, 3, 1]

print_list(l)
print(f'Sum is {sum(l)}')
print(f'Maximum is {max(l)}')
