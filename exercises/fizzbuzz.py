import sys
import unittest
from unittest.mock import patch, call


def fizzbuzz():
    """
    Print out the results of playing FizzBuzz up to 20.

    In FizzBuzz, you count up to a specific number.
    If the number is a multiple of three, print Fizz.
    If the number is a multiple of five, print Buzz.
    If the number is a multiple of three and five, print FizzBuzz.
    If none of the above sentences is true, just print the number.
    """
    pass


# =========
#  TESTING
# =========
class DecisionMakingTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_fizz_buzz(self, mocked_print):
        fizzbuzz()

        expected_prints = [
            call('1'), call('2'), call('Fizz'), call('4'), call('Buzz'),
            call('Fizz'), call('7'), call('8'), call('Fizz'), call('Buzz'),
            call('11'), call('Fizz'), call('13'), call('14'), call('FizzBuzz'),
            call('16'), call('17'), call('Fizz'), call('19'), call('Buzz')
        ]
        actual_prints = mocked_print.mock_calls

        self.assertEqual(len(expected_prints), len(actual_prints))

        for expected, actual in zip(expected_prints, actual_prints):
            self.assertEqual(expected, actual)


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    unittest.main(argv=sys.argv[:1])
