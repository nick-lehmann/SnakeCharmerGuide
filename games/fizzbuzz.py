"""
Fizzbuzz is a math game for children to teach them about division. Write a function that plays the fizzbuzz game. It takes an argument that is the upper limit for the game.

Fizzbuzz is played like this:
- You start at 1
- With each turn, you count up by one.
- If the number is divisible by 3, print "Fizz"
- If the number is divisible by 5, print "Buzz"
- If the number is divisible by 3 and 5, print "Fizzbuzz"
- If none of the three conditions is true, just print the number

Example: n = 20
=> 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz
"""

def fizzbuzz(n):
	for i in range(1, n):
		if i % 3 == 0 and i % 5 == 0:
			print("Fizzbuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

fizzbuzz(20)