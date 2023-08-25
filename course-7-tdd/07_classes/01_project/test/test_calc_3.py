import unittest
from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculatorAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up class ...")
        cls.calc = SimpleMathCalculator()

    @classmethod
    def tearDownClass(cls):
        print("Tearing down ...")
        del cls.calc

    def test_add_int(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_add_float(self):
        self.assertEqual(self.calc.add(3.0, 4.0), 7.0)

    def test_add_both_negative(self):
        self.assertEqual(self.calc.add(-3, -4), -7)


class TestSimpleMathCalculatorSubtract(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up class ...")
        cls.calc = SimpleMathCalculator()

    def test_sub_int(self):
        self.assertEqual(self.calc.subtract(3, 4), -1)

    def test_sub_float(self):
        self.assertEqual(self.calc.subtract(2.5, 4.5), -2.0)

