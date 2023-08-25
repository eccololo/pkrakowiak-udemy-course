import unittest
from calculator.calc_math import SimpleMathCalculator


def setUpModule():
    print("Setting up ...")
    global calc
    calc = SimpleMathCalculator()


def tearDownModule():
    print("Tearing down ...")
    global calc
    del calc


class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(calc.subtract(3, 4), -1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 4), 12)
