import unittest
from ..src.Assignment10.util import cnt
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(cnt(["apple","banana","apple"]), [2, 1])  # add assertion here

if __name__ == '__main__':
    unittest.main()
