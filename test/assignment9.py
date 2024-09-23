import unittest
from ..src.Assignment9.util import split_remove_duplicates
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(split_remove_duplicates("apppllleee",3), ['ap', 'lp', 'el', 'e'])  # add assertion here

if __name__ == '__main__':
    unittest.main()
