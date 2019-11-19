import unittest
from typing import List


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


# =========
#  TESTING
# =========
class StringMethodsTestCase(unittest.TestCase):
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


unittest.main()
