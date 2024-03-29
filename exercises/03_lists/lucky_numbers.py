""" Determine if a number is lucky. """
import unittest


def is_lucky(number: int) -> bool:
    """
    Determine if the given ticket number is lucky.

    A ticket number always consists of an even amount of digits.
    It is considered lucky if the sum of the first half of digits
    is the same as the sum of the second half.

    TIP: The sum() takes a list as an argument and returns the sum
    of all elements.
    """
    pass


# =========
#  TESTING
# =========
class LuckyNumberTestCase(unittest.TestCase):
    def test_is_lucky(self):
        self.assertTrue(is_lucky(1230))
        self.assertTrue(is_lucky(11))
        self.assertTrue(is_lucky(678876))
        self.assertTrue(is_lucky(99999999))

        self.assertFalse(is_lucky(10))
        self.assertFalse(is_lucky(234789))
        self.assertFalse(is_lucky(1002))


unittest.main()
