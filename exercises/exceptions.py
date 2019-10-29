import sys
import unittest
import tempfile


def divide(dividend: int, divisor: int) -> float:
    """
    Return the result of the division but raise an error
    if the divisor is zero.

    Note: The appropriate error class is ZeroDivisionError.
    """
    pass


def count_lines_of_files(filename) -> int:
    """
    Return the number of lines in the file with the
    given filename.

    If the given file does not exist, catch the exception and return zero.

    Note: Use the builtin open() function and the associated readlines()
    function to read the lines from the file.
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


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    unittest.main(argv=sys.argv[:1])
