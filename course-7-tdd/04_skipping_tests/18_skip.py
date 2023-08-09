import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual("aws".upper(), "AWS")

    @unittest.skip("Always skipping ...")
    def test_case_2(self):
        self.assertEqual("aws".upper(), "AWS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
