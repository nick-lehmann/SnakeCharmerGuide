import sys
import unittest


def divide(dividend: int, divisor: int) -> float:
    """
    Return the result of the division but raise an error
    if the divisor is zero.

    Note: The appropriate error class is ZeroDivisionError.
    """
    pass


def count_lines_of_files(filename: str) -> int:
    """
    Return the number of lines in the file with the
    given filename.

    If the given file does not exist, catch the exception and return zero.

    Note: Use the builtin open() function and the associated readlines()
    function to read the lines from the file.
    """
    pass


def sell_vodka(money: int, age: int):
    """
    Try to sell vodka to a person with the given age.

    If the person is underage, throw a PersonTooYoungException.
    If the person does not have enough money, throw an NotEnoughMoneyException.

    The price for one bottle of vodka is 10. Return true if selling was
    successful.
    """
    pass


class ExceptionTestCase(unittest.TestCase):
    def test_division(self):
        self.assertEqual(divide(8, 4), 2)
        self.assertEqual(divide(4, 4), 1)

        with self.assertRaises(ZeroDivisionError) as _:
            divide(1, 0)

    def test_count_lines_of_code(self):
        self.assertEqual(count_lines_of_files('./dummy.py'), 6)
        self.assertEqual(count_lines_of_files('./does_not_exist.py'), 0)

    def test_sell_vodka(self):
        self.assertTrue(sell_vodka(100, 40))
        self.assertTrue(sell_vodka(10, 18))

        with self.assertRaises(Exception) as context:
            sell_vodka(100, 5)
        self.assertEqual(type(context.exception).__name__, 'PersonTooYoungException')

        with self.assertRaises(Exception) as context:
            sell_vodka(5, 20)
        self.assertEqual(type(context.exception).__name__, 'NotEnoughMoneyException')


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    unittest.main(argv=sys.argv[:1])
