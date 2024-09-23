import unittest

from ..src.Assignment6.util import tt

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(tt(), "The difference in seconds is: 114285 seconds")  # add assertion here

if __name__ == '__main__':
    unittest.main() 
