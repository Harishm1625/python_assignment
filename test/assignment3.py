import unittest
from python_assignment.src.Assignment3.util import mutio

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(mutio(),"Aplle")  # add assertion here


if __name__ == '__main__':
    unittest.main()
