🐍 Snake Charmer Guide
======================

In this repo you will find all material related to the Python beginner course held at the TU Dresden in the winter term 2019/20.

## ✈️ Overview

- Introduction & Installation
- Basics
    - Variables & Typen
    - If & Else
    - Functions
    - For & While
 - Write your own code
    - Dice simulator
    - Guess a number
- Classes
- Imports, Modules
- External Packages & PIP


## 🚀 Project ideas

By the end of this course, every

- 📄 PDF Merger & Downloader Utility
- 📹 Youtube Downloader
- 🤖 Telegram Bot

If you have an idea for a project that you would like to see realised and explained, we are open for suggestions.


## 💪🏻 Exercises

In the exercises folder, you will find many prepared Python files that already include scaffolds. 

Say you want to run the `factorial.py` exercise. After navigating to the directory with all the exercises, the following command will run the code.

```bash
python3 factorial.py
```

*NOTE:* Depending on your operating system and installation method, the interpreter could also be called `python` or ``python38``.

This will only run the code that is not inside any function. However, each exercise will include prepared tests that allow you to check if your implementation is correct. To trigger the test execution, just add `test` to the command.

```bash
python3 factorial.py test
```


## 🎓 Anatomy of an exercise

All exercises follow a similar structure but contain lines you might not understand at the start of this course. Don't worry, things will start to become a lot clearer during the course. Nevertheless, the structure will be explained here, for the sake of completeness.

```python
import sys
import unittest
```

These two lines import functionality implemented by somebody else. In this case, the `sys` and `unittest` module are included with python and maintained by the core developers. The `sys` module provides access to functionality provided by your operating system and is needed to start the tests when `test` is given as the first argument. The `unittest` module allows you to test your code automatically and is responsible for actually running the tests. Using modules will be explained in the last two chapters of this course.

```python
def factorial(num: int) -> int:
    """
    Return the factorial of the given number.
    """
    pass
```

Each exercise will contain one or more functions that you should implement. All function parameters (`num`) have their type annotated so you know what type of input you can expected (`int`). The return value is also annotated to let you know what type of output your implementation should produce. 

The description is what the function should actually do is given as a docstring (the thing between the triple quotes). No exercise requires you to have any prior knowledge about the topic of the exercise, as the explanation found here should be sufficient.

The `pass` statement is just a placeholder and should be replaced with your implementation.

```python
class FactorialTestCase(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(20), 2432902008176640000)
```

When you use the `unittest` module, it is necessary to group your tests into test cases. These are represented as classes (`FactorialTestCase`) and the single tests are written as methods of this class (`test_factorial`). All test cases should inherit from the `TestCase` class.

The thing that is important for you right at the beginning are all lines containing an `assertEqual` or similar. They represent the expected behaviour of your implementation and cause tests to fail when the generated output differs from what is expected.

```python
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    unittest.main(argv=sys.argv[:1])
```

The last two lines are the reason why invoking the script with `test` as the first argument will run the defined tests.
