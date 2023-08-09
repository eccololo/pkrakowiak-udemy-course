import unittest


class Person():

    def __init__(self, name):
        self.name = name


class Worker(Person):
    pass


class TestPerson(unittest.TestCase):

    def test_case_1(self):
        self.assertIsInstance(Person, type)

    def test_case_2(self):
        person = Person("Mateusz")
        self.assertIsInstance(person, Person)

    def test_case_3(self):
        person = Person("Mateusz")
        self.assertNotIsInstance(person, str)


class TestWorker(unittest.TestCase):

    def test_case_1(self):
        worker = Worker("Mateusz")
        self.assertIsInstance(worker, Worker)

    def test_case_2(self):
        worker = Worker("Mateusz")
        self.assertIsInstance(worker, Person)

    def test_case_3(self):
        worker = Worker("Mateusz")
        self.assertNotIsInstance(worker, int)


if __name__ == "__main__":
    unittest.main(verbosity=2)
