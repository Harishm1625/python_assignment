import unittest

from ..src.Assignment11.util import validation
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(validation(), ["hari@gmail.com"])  # add assertion here


if __name__ == '__main__':
    unittest.main()
