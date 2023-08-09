import unittest
from rectangle import area, perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, "Expected area is not equal to calculated.")

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, '5')

    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area, -1, 5)
        self.assertRaises(ValueError, area, 4, -1)



class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(perimeter(4, 5), 18, "Expected perimeter is not equal to calculated.")

    def test_perimeter_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, perimeter, '4', 5)
        self.assertRaises(TypeError, perimeter, 4, '5')

    def test_perimeter_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, perimeter, -1, 5)
        self.assertRaises(ValueError, perimeter, 4, -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
