import sys
import unittest


def is_even(number: int) -> bool:
    """
    Decide if the given number is even.
    """
    pass


def is_odd(number: int) -> bool:
    """
    Decide if the given number is odd.
    """
    pass


# =========
#  TESTING
# =========
class EvenOddTestCase(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(10))
        self.assertTrue(is_even(1462702))

        self.assertFalse(is_even(1))
        self.assertFalse(is_even(5))
        self.assertFalse(is_even(11))
        self.assertFalse(is_even(6456281))

    def test_is_odd(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(11))
        self.assertTrue(is_odd(6456281))

        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(10))
        self.assertFalse(is_odd(1462702))


unittest.main()
