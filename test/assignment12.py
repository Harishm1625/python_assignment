import unittest
from ..src.Assignment12.util import nid

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(nid(), 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
