import unittest

from ..src.Assignment8.util import float_format
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(float_format(), "(array([6.]), array([5.]), array([6.]))")  # add assertion here


if __name__ == '__main__':
    unittest.main()
