import sys
import unittest
from typing import List


def concatenate_with_whitespace(s1: str, s2: str) -> str:
    """
    Concatenates the two given string with a whitespace
    and return the result.
    """
    pass


def convert_case(input_string: str, conversion: str) -> str:
    """
    Convert the given string according to the conversion parameter.

    Conversion parameters are:
    - upper
    - lower
    """
    pass


# ==============================
#  Comma separated values (CSV)
# ==============================
#
# CSV is a format where each line represents a data entry and
# on each line the values are separated by a comma.
#
# E.g. representation of three people
# Max,Mustermann,18,Dresden
# Ana,Bolika,20,Leipzig
# Christoph,Smaul,19,Berlin
#
# Tip: The representation of the newline ("Enter") is '\n'

def store_to_csv(raw_data: List[List[str]]) -> str:
    """
    Return the given data in csv.

    The input is a list where each entry is a list of strings.
    """
    pass


def load_from_csv(data: str) -> List[List[str]]:
    """
    Given a csv string, return the data as a list of lists.
    """
    pass


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

    def test_store_csv(self):
        raw_data = [
            ['Max', 'Mustermann', '18', 'Dresden'],
            ['Ana', 'Bolika', '20', 'Leipzig'],
            ['Christoph', 'Smaul', '19', 'Berlin']
        ]

        self.assertEqual(
            store_to_csv(raw_data),
            """
            Max,Mustermann,18,Dresden
            Ana,Bolika,20,Leipzig
            Christoph,Smaul,19,Berlin
            """
        )

    def test_load_csv(self):
        raw_data = """
        Max,Mustermann,18,Dresden
        Ana,Bolika,20,Leipzig
        Christoph,Smaul,19,Berlin
        """

        self.assertEqual(
            load_from_csv(raw_data),
            [
                ['Max', 'Mustermann', '18', 'Dresden'],
                ['Ana', 'Bolika', '20', 'Leipzig'],
                ['Christoph', 'Smaul', '19', 'Berlin']
            ]
        )


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    unittest.main()
