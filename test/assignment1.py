import unittest
from python_assignment.src.Assignment1.util import fnd_avg

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertGreater(fnd_avg(), 15)  # add assertion here


if __name__ == '__main__':
    unittest.main()
