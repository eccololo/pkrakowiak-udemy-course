import sys
import unittest
from calculator.calc_math import SimpleMathCalculator

path = r'C:\Users\Mateusz\Documents\IT Library\Github\Projects\Python\Pawel Krakowiak Python Course\course-7-tdd\07_classes\02_project\tests'
sys.path.append(path)

class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.add(3, 4), 7)

    def test_subtract(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.subtract(3, 4), -1)

    def test_multiply(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.multiply(3, 4), 12)
