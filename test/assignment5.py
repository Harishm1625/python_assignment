import unittest
from python_assignment.src.Assignment5.util import calender_module

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calender_module("16 06 2001"), "Saturday")  # add assertion here

if __name__ == '__main__':
    unittest.main()



