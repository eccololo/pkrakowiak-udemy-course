import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual("aws".upper(), "AWS", "The strings are not the same.")

    def test_case_2(self):
        self.assertEqual("aws".upper(), "AWS", "The strings are not the same.")

    def test_case_3(self):
        self.assertEqual("3.9.0".split("."), ["3", "9", 0])

    def test_case_4(self):
        self.assertEqual(tuple("3.9.0".split(".")), ("3", "9", 0))

    def test_case_5(self):
        self.assertEqual({3, 4}, {4, 3, 5})

    def test_case_6(self):
        self.assertNotEqual("aws".upper(), "aws")


if __name__ == '__main__':
    unittest.main(verbosity=2)
