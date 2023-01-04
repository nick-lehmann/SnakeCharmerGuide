# OUTLINE

## ✈️ Overview

- Beginner basics (variables, if/else, loops, functions), Naming conventions
- Datastructures (list, dict, tuple, sets, iteration techniques, nested variants)
- Map, Reduce, Filter, Comprehension
- Classes (Basics, Inheritance, Static methods, dunder)
- Type Hints
- String manipulation
- Standard library
  - CSV, JSON
  - Date(Time)
  - Random
  - File access
- Exceptions
- Enum
- Modules (Structure e.g. **init**, pip(env))

Bonus + Nice to have:

- Generator, Iterators (`itertools`)
- Decorator, First-class functions
- Async/await
- Multiprocessing
- Idiomatic python (documentation, annotation, unittesting)
- Debugging strategies (e.g. debugger)
- Implement a project (see following ideas)

Project ideas:

- spotify evaluator
- telegram bot to scrape mensa meals
- [wordle](https://www.nytimes.com/games/wordle/index.html) solver
- 2048 terminal game (hard on windows)

## Session 1 (20.10.2022)

Learning goals:

- Make sure everyone can run a python script
- Everyone is familiar with python basics (variables, if/else, loops, functions)

Outline:

- Ask about language of course
- Quick introduction of tutors
- Talk about form (results, questions we have about answers, wishes for topics)
- Tell people about the format of the lessons
- Ask who has no python installation
- Slides about variables & if/else + "Ninja" Game
- Slides about loops + "Pizza" Game
- Slides about functions + "How far" Game

## Session 2 (27.10.2022)

Learning goals:

- Datastructures
  - list/tuples
  - sets
  - dict
  - iteration techniques
  - nested datastructures
- Have a look at the python documentation

Outline:

- Fizzbuzz as warmup
- Slides about lists + look at python docs
- [Fishes](games/lanternfish.py) game
- Sets + Bonus in fishes game
- Slides about dict
- [Student](games/students.py) game
- Sum helper methods (max, min, sum)

## Session 3 (03.11.2022)

Learning goals:

- Dicts
- Iterating dicts
- Nested data structures

Outline:

- Slides about dict
- [Student](games/students.py) game
- Sum helper methods (max, min, sum)
- [Built in functions](https://docs.python.org/3/library/functions.html#built-in-functions)

- Map, Reduce, Filter
- Use naive first, then comprehension
- List & Dict comprehension

## Session 4 (10.11.2022)

Learning goals:

- Map, Reduce, Filter
- Comprehensions
- Lambda

Outline:

- List exercise with map, filter, int, abs, sum
  - Show the basics
  - Refactor with list comprehension
  - Mention that it also works for dicts, example exponent
- Sorted
  - Show how it works with list, then with dict
  - Mate
- Lambda

## Session 5 (17.11.2022)

Learning goals:

- Basics of classes and OOP

Outline:

- Show reference solution for Mate game (5min)
- Motivational example why you need it (how far game) (10min)
- Slides about classes (10min)
- Human exercise (30min)
- Point exercise (30min)

## Session 6 (24.11.2022)

Learning goals:

- Dunder methods
- Inheritance

Outline:

- Show solution to simple Point + give time to finish (10 min)
- Slides dunder (5min)
- Extend point class with arithmetic dunder methods and string formatting (30min)
- Str, Len, eq
- Add / Sub
- Inheritance slides (5 min)
- Human reloaded (30min)

## Session 7 (01.12.2022)

Learning goals:

- Inheritance

Outline:

- Remember naming conventions by example in editor (5min)
- Show slides about inheritance (10min)
- Show inheritance and `isinstance` in the editor (10min)
- Classroom game
  - Base classes (20min)
  - 4 & 5 (20min)
  - Bonus (20min)

## Session 8 (08.12.2022)

Learning goals:

- Exceptions
- First imports

Outline:

- Solution to the classroom exercise (no bonus) (5min)
- Slides exceptions (10min)
- Basic except exercise (15min)
- Slides import (10min)
- Dice game (45min)

## Session 9 (15.12.2022)

Learning goals:

- Modules

Outline:

- Finish up the dice game & show solution (10min)
- Slides about imports plus show how imports are composed on the filesystem (10min)
- Show how imports are done. (10min)
- Math adventures (45min)


## Session 10 (05.01.2023)

Learning goals:

- Modules from PyPi
- Basic networking with requests
- Basic understanding of APIs

Outline:

- Show PyPi & check pip with everyone (5min)
- Explore OpenMensa API (15min)
- Menu game (60min)
- If time: Introduction to async