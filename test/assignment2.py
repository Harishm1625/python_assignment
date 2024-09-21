import unittest
from python_assignment.src.Assignment2.util import secondlrg

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertLess(secondlrg(), 100)  # add assertion here


if __name__ == '__main__':
    unittest.main()
