import unittest


def setUpModule():
    print("Establishing connection with DB ...")


def tearDownModule():
    print("Closing DB connection ...")


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f"Setting up class ...{cls.__name__}")

    @classmethod
    def tearDownClass(cls):
        print(f"Tearing down class ...{cls.__name__}")

    def setUp(self):
        print("Setting up ...")

    def tearDown(self):
        print("Tearing down ...")

    def test_case_1(self):
        self.assertEqual("John Smith".split(), ["John", "Smith"])

    def test_case_2(self):
        self.assertEqual("John Smith".split(), ["John", "Smith"])


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual("3.9".split("."), ["3", "9"])


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual("#".join(["sport", "gym"]), "sport#gym")


if __name__ == "__main__":
    unittest.main(verbosity=2)
