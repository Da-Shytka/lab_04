import unittest
from lib import count_equals

class TestCountEquals(unittest.TestCase):

    def test_def(self):
        mas = [[2, 5, 7, 7, 8, 2, "a", "a", "a"],
               [2, 5, 7, 10],
               ["a", 2, 7]]
        count_mas = len(mas)
        self.assertEqual(count_equals(mas, count_mas), [3, 3, 2])
        