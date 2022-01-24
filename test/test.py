from src.foo import add_numbers
import unittest

class UnittestTests(unittest.TestCase):


    def test_add(self):
        assert add_numbers(500, 3.4) == 503.4
