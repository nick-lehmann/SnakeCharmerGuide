""" Decide what to do on a weekend. """
import unittest


def weekend_activity(friend_available: bool, nice_weather: bool) -> str:
    """
    Return the appropriate weekend activity based on whether a friend
    is available and the upcoming weather.

    Possible return values are:
    - Go for a walk
    - Swimming
    # - Homework
    - Cinema
    """
    pass


# =========
#  TESTING
# =========
class WeekendActivityTestCase(unittest.TestCase):
    def test_weekend_activity(self):
        self.assertEqual(
            weekend_activity(True, True),
            'Swimming'
        )
        self.assertEqual(
            weekend_activity(True, False),
            'Cinema'
        )
        self.assertEqual(
            weekend_activity(False, True),
            'Go for a walk'
        )
        self.assertEqual(
            weekend_activity(False, False),
            'Homework'
        )


unittest.main()
