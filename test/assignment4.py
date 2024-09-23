import unittest

from python_assignment.src.Assignment4.util import str_format


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(str_format(1),['1 1 1 1'] )  # add assertion here


if __name__ == '__main__':
    unittest.main()
