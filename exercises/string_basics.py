import sys
import unittest


def concatenate_with_whitespace(s1, s2):
    """
    Concatenates the two given string with a whitespace
    and return the result.
    """
    pass


def convert_case(input_string, conversion):
    """
    Convert the given string according to the conversion parameter.

    Conversion parameters are:
    - upper
    - lower
    """
    pass


# =========
#  TESTING
# =========
class StringMethodsTestCase(unittest.TestCase):
    def test_concatenate(self):
        self.assertEqual(
            concatenate_with_whitespace('hello', 'world'),
            'hello world'
        )
        self.assertEqual(
            concatenate_with_whitespace('Max', 'Mustermann'),
            'Max Mustermann'
        )

    def test_convert_case(self):
        self.assertEqual(
            convert_case('hello world', 'upper'),
            'HELLO WORLD'
        )
        self.assertEqual(
            convert_case('max Mustermann', 'upper'),
            'MAX MUSTERMANN'
        )
        self.assertEqual(
            convert_case('HELLO', 'upper'),
            'HELLO'
        )

        self.assertEqual(
            convert_case('HELLO WORLD', 'lower'),
            'hello world'
        )
        self.assertEqual(
            convert_case('University', 'lower'),
            'university'
        )


unittest.main()
