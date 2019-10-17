import sys
import unittest


# ==========
#  EXERCISE
# ==========
def check_palindrome(input_string: str) -> bool:
    """
    Check if the given string is a palindrome.

    A palindrome is a word that is the same whether it is
    read from left to right or the other way around.
    """
    pass


# =======
#  TESTS
# =======
class PalindromeTestCase(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(check_palindrome('aabaa'))
        self.assertTrue(check_palindrome('a'))
        self.assertTrue(check_palindrome(' '))
        self.assertTrue(check_palindrome('abacaba'))

        self.assertFalse(check_palindrome('abac'))
        self.assertFalse(check_palindrome('az'))
        self.assertFalse(check_palindrome('hello world'))


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    unittest.main()
