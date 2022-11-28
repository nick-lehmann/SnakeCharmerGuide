# Games

The solutions can be found in the relative files. But it's much more fun to solve them alone! You will learn more 😉

![Games](https://images.unsplash.com/photo-1545558014-8692077e9b5c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80)

### 🐄 Milka [If/Else]

Milka the cow needs 10 grass to do 1 chocolate
2 Grass grow from 1 rain.

1. Define a variable called "rain" and one called "grass"
2. With an "if" check if there is enough grass to make a chocolate
3. If enough, print how many chocolates we can have, otherwise be sad

Bonus Points: Give the cow a name and print it

### 🤺 Ninjas [If/Else]

The wall has been breached and cobras are attacking the castle 🏰
We see that there are 50 cobras approaching 🐍
Fortunately we have special ninjas that can defeat the cobras 🥷
Every ninja can defeat 3 cobras.
Can we defeat all the cobras with the ninjas we have?

1. Define a variable "ninjas" and one "cobras" and print if we win or loose based on the variables

Bonus Points: Say how many more ninjas do we need to win the fight!

### 👨‍👧‍👧 Pairs [If/Else]

All the students must get together in groups.
Are all students in a group or is there someone alone?

1. Define a variable "students" and one "group_size"
2. Check with the modulo operator "%" if there is someone left out in the gruop

Bonus Points: How many additional students do you need to fill the group?
Bonus Bonus Points: What group sizes are possible so that no one is left out?

### 🙎‍♀️ The new friend [Lists]

We have a list of friends
"Charlie" is a new friend, but in the beginning she is at the end.
We all like Charlie so we put her in the middle of our friends.

1. Create a list with 4 names (Alice, Bob, Diana, Elisa)
2. Put Charlie inside the friend list
3. Move Charlie to the middle

### 🍕 Pizza [Loops]

Mario is eating a pizza.
The pizza is so tasty that every time he eats a slice he wants to say "Mhhhhhh".
Every time he eats a slice his hunger gets lowered by 1.
If he is full, he stops eating and says "I'm full 🤤"
When he is finished he says "Mamma mia! Buonissima! 😋"

1. Define a variable "slices" and "hunger"
2. For each slice say "mhhh"
3. Check if he has hunger left
4. When finished say "Mamma ..."

Bonus Points: say if he is still hungry after eating

### 🚂 Train Driver [Loops]

You are driving a train from Berlin to Paris.
On the way to Paris you will stop in Hamburg, Amsterdam and Brussels before arriving in Paris.
Every time you depart you will need to tell the passengers that you are departing and what the next stop will be.
In Paris tell the passengers that is the last stop

Bonus Points: Do all the prints inside the loop.

### ⛽️ How far can we make it? [Functions]

How far can our car drive?
Renee is driving when she realizes that her tank is almost empty.
She knows her car burns a certain amount of liters of gas every 100km.
She also knows the distance to the next gas station.
Will she make it or will she be stranded?

Renee drives a Jaguar F-TYPE R that consumes 10,9 l/100km.
The next gas station is 420km away.
She has 40 Liters of gas left

Arnold drives a Fiat 500 that consumes 4,9 l/100km.
The next gas station is 285km away.
He has 15 Liters of gas left

Annabelle drives a Renault Espace that consumes 5,8 l/100km.
The next gas station is 69km away.
She has 4 Liters of gas left

Bonus Points: Will the drivers make it if they drive slowly? (+10% efficiency)

### 🙍🏼‍️🙍🏼‍️🙍🏼‍ The oldest [Dictionaries]

You have some students and know how old they are. Mike is 19, Peter is 20, Michelle is 22 and Nicole is 20.

1. Save the age of each student in a dictionary.
2. Add the student Max who is 18 years old.
3. Today is Michelle's birthday, so make Michelle her one year older.
4. Choose a name and check if there is a student with this name.
5. Find the oldest student and print his name and age.

### ⛰📃✂️ Rock-Paper-Scissors [Dictionaries]

You want to play rock-paper-scissors against the computer.

1. Define a dictionary for each player that stores its name and current score.
2. Ask the player about his or her name and ask how many round should be played.
3. Each round, ask the player for his or her choice. The computer should pick a random choice.
4. Evaluate each round and print who has won.

Bonus Points: Accept different spelling of each choice ('rock', 'Rock', 'rOcK') and maybe even abbreviations.

### 🙍🏼‍♂️ Human [Classes]

1. Implement a class `Human` class with just two attributes: `name` and `age`. Do not forget the constructor.
2. Add a method for saying hi. It should print out the name and the age.
3. Add a method for having a birthday that increases the age of the current human by one.
4. Add a list of hobbies to your Human class (remember the constructor) and include the hobbies in the `say_hi` method.
5. Add a method has_hobby to find out, if the given hobby is one of the humans' hobbies. Return a boolean (`True` or `False`).
6. Add a method to add a human's hobby. If the human already has the hobby, print an appropriate message and do not add it. Otherwise, add it.

### 👨‍👩‍👦‍👦 Classroom [Classes, Inheritance]

1. Create (or copy from the `human.py`) a `Human` class.

- Add a `name` and `age` properties.
- Add a `__str__` which returns the name and age.
- Add a `birthday` method which increases the age by 1.

2. Create a class `Student` that inherits from `Human`

- Add a property `school`, which should represent the school the student is enrolled at.
- Extend the `__str__` method to also print that this Human is a student that is studying at `school`.
- Add a `take_notes` method.

3. Create a class `Teacher` that also inherits `Human`.

- Add the properties `school` and `subject`.
- Extend the `__str__` method to also print what the teacher is teaching at what school.
- Add `teach` method.

4. Create a list `classroom` with 2 students and 1 teacher.

- Write a method that checks if the classroom is complete (At least 2 students and 1 teacher).
- Print wether the classroom is complete or not.

5. It's time to hold a lesson!

- Create a method `hold_class` that takes our `classroom` and for each Human either `takes_notes` or `teaches`

_BONUS:_

- Instead of 4 & 5, write a class `ClassRoom` that checks if the classroom is valid on initialization.
- Add a `hold_class` method that does the same thing as in 5.

### 📌 Point [Classes]

1. Create a Point class that has two attributes, x and y. Remember the constructor.
2. Implement an add method that takes another point, adds this one to itself and returns a new Point that is the result of the addition.
3. Implement a method that calculates the distance from itself to another point using Pythagoras. The other point should be given as a parameter. Return the calculated distance as a number.
4. Implement a method that calculates the distance from the point to the origin (0,0). No parameters are needed.
5. Given p1 = Point(1,2), p2 = Point(2,4) and p3 = Point(5,1). Add all points to p. Calculate the distance of p to p4 = Point(10,10) and (0,0). (Results should be `3.6` and `10.6` respectively)

INFO: Do not forget to add the `self` parameter to every method.

INFO: Everything should be implemented in the class. No standalone functions are needed (or allowed ;) ).

INFO: Raising a number to a power is done using the `**` operator, e.g. `2 ** 3 == 8`. If you want to calculate the square root, raise the number to `1/2` for now.

### 📌 Point2 [Classes]

Implement `dunder` methods on the `Point` class to make it more convenient to work with.

1. Add a string representation.
2. Make the addition of two points easier. (Check the `sum` builtin with multiple points)
3. Let's assume we have to find the distance between two points very often. Implement subtraction between two points to return the distance between them.
4. It's also very common to find the distance of a point related to the origin. Use the `float` function to do that.
5. Let's compare points. The smaller point is the one closer to the origin. Implement the corresponding dunder method. (check the `min` function with multiple points)

Info: You find documentation for the `dunder` methods here: https://docs.python.org/3/reference/datamodel.html#basic-customization.

### 🧮 Math adventure

You're going to implement a few basic math methods yourself! Hurray 🥳

The goal is simple: Print a list as bullet points (each item has a dash "-" in front) and then both the
sum and the maximum of the list. The function for outputting a list as bullet points should be in its own
module and the `sum()` and `max()` function should be in their own module as well.

Tasks:

1. Add three files/modules: one for the output function, one for the math functions and one where you write your code that uses
   the other two modules (e.g. `main.py`).
2. Think of a list of integers. What is its maximum element and its sum?
3. Write the output function that prints a list as bullet points.
4. Write the `max()` function that finds the maximum of the given list.
5. Write the `sum()` function that finds the sum of the given list.

### 🎲 Guess my number

You are going to implement the "Guess my number" play. When the game starts, the computer chooses a random number
from a given range (e.g. one to six, but any other will do). Then, the user has three rounds to guess the number.
After entering his or her guess, the user gets a message if the guess was too low or too high. If the guess was correct,
the game is over and he/she has won. Otherwise, the next rounds starts. If the user did not guess the number after three
rounds, he/she has lost.

NOTE: Use the [random](https://docs.python.org/3/library/random.html) package from the standard library.
BONUS: Let the user choose the range of numbers the secret number can be chosen from.

### 🔐 Password Generator

Implement your own secure password generator. Ask the user how long the password should be and print the generated
password. For security reasons, every character should have the same probability to end up in the password.

NOTE: Use the [string](https://docs.python.org/3/library/string.html) module to get a list of possible characters
and the [random](https://docs.python.org/3/library/random.html) module to generate the password.
NOTE: Take a look at the [`join()` method](https://docs.python.org/3/library/stdtypes.html#str.join)

### Fizzbuzz

fizzbuzz is a math game for children to teach them about division. Write a function that plays the fizzbuzz game. It takes an argument that is the upper limit for the game.

fizzbuzz is played like this:

- You start at 1
- With each turn, you count up by one.
- If the number is divisible by 3, print "Fizz"
- If the number is divisible by 5, print "Buzz"
- If the number is divisible by 3 and 5, print "Fizzbuzz"
- If none of the three conditions is true, just print the number

Example: n = 20
=> 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz

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

## Students

You have a course with students, each having a "name", an "age" and a list of "grades", e.g.:

```python
# 1.0 is the best grade, 6.0 the worst
students = [
  {
    'name': 'John',
    'age': 21,
    'grades': [1.3, 2.7, 1.0]
  },
  {
    'name': 'Michelle',
    'age': 25,
    'grades': [1.0, 3.7, 2.3]
  },
  {
    'name': 'Thomas',
    'age': 41,
    'grades': [2.3, 2.7, 2.0]
  }
]
```

(It is best to put the information in a variable, don't use `input()` here)

And now you want to gather some information about your course. It is enough to print the information to the console after each other.

**Part 1**

1. For your teaching, you need a list of names.
2. Your memory got quite bad as you have grown older. Is there a 'Thomas' in your course?
3. Since your students vary in age, you want to know the average age of your class.
4. Some students perform better, some worse. You would like to know the average grade of each student. Save that as a new key in the dictionary, e.g. `average`.
5. Damn! The other class is better than yours. To make you look like a better teacher, you decide to remove the worst grade for each student. Do so and print recalculate the averages again.
6. Now, you notice that some students are still not doing well. You want to print the names of all students (like in task 4) with an average grade bigger than 2.0.

**Part 2**

1. Sort the names of the students alphabetically.
2. Print the student names sorted by their average grade.

## Exercise Session 4

**Part 1: Map, Filter**

```python
numbers = ['1', '-5', '3', '0', '-2', '-4', '7', '0', '3', '-1', '2', '8']
```

- Do not use while or for loops.
- Convert the list to int, filter any number that is not 7 and then sum it up. Solution: `5`.
- Now use the absolute value of the numbers. Solution: `29`.

Use the [built in functions](https://docs.python.org/3/library/functions.html) like `filter`, `map`, `int`, `abs` and `sum`.

**Part 2: Sort**

```python
drinks = [
    {"name": "Kolle-Mate", "caffeine": 20, "price": 2.37},
    {"name": "Biozisch Mate", "caffeine": 20, "price": 2.97},
    {"name": "Muntermate", "caffeine": 20, "price": 7.65},
    {"name": "Club Mate", "caffeine": 20, "price": 1.58},
    {"name": "Flora Mate", "caffeine": 18, "price": 1.95},
    {"name": "1337", "caffeine": 29, "price": 1},
    {"name": "Maya Mate", "caffeine": 21.5, "price": 1.95},
    {"name": "Mio Mate", "caffeine": 20, "price": 1.18},
]
```

Use the [built in function](https://docs.python.org/3/library/functions.html) `sorted`.

- For each Mate define a new key `power` that determines how much caffeine/price there is.
- Sort the list by the one with the most caffeine.
- Print the Mate with the most power, and the one with the lowest.
