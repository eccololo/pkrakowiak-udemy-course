import unittest


def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


# Enter your solution here

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_valid_input(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2)
        self.assertEqual(calculate_average([5, 5, 5]), 2)
        self.assertEqual(calculate_average([4, 10, 7]), 7)

    def test_calculate_average_empty_input(self):
        self.assertEqual(calculate_average([]), None)

    def test_calculate_average_invalid_input(self):
        self.assertRaises(TypeError, calculate_average, [1, 4, True])
        self.assertRaises(TypeError, calculate_average, [6, "a", False])
        self.assertRaises(TypeError, calculate_average, ["h", "m", 3])


unittest.main()
