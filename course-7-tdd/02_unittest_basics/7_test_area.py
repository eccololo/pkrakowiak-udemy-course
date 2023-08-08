import unittest


def area(w, h):
    if not (isinstance(w, (int, float)) and isinstance(h, (int, float))):
        raise TypeError("Width and height must be value of type int or float.")

    if not (w > 0 and h > 0):
        raise ValueError("Width and height must be value greater than 0.")

    return w * h


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, "Expected area is not equal to calculated.")

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, '5')

    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area, -1, 5)
        self.assertRaises(ValueError, area, 4, -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
