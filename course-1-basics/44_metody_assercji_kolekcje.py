import unittest


class SimpleTest(unittest.TestCase):

    def test_1(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3, 4])

    def test_2(self):
        self.assertTupleEqual((1, 2), (1, 2, 3))

    def test_3(self):
        self.assertSetEqual({4, 5}, {4, 5, 6})

    def test_4(self):
        self.assertDictEqual({"a": 1, "b": 2}, {"a": 1, "b": 2, "c": 3})


if __name__ == '__main__':
    unittest.main()
