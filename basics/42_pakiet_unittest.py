import unittest


def add_numbers(x, y):
    return x + y


class SimpleTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add_numbers(3, 5), 8, msg="Powinno być 8.")


if __name__ == '__main__':
    unittest.main()
