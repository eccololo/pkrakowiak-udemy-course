import unittest
import sys


class TestClass(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("win"), "Required Windows ...")
    def test_case_1(self):
        self.assertEqual("aws".upper(), "AWS")

    @unittest.skipUnless(sys.platform.startswith("linux"), "Required Linux ...")
    def test_case_2(self):
        self.assertEqual("aws".upper(), "AWS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
