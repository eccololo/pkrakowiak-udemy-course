import unittest


class SimpleTest(unittest.TestCase):
    x = 6
    y = 8

    @unittest.skip("Powod: Ponieważ pomijamy.")
    def test_add(self):
        wynik = self.x + self.y
        self.assertEqual(wynik, 8)

    @unittest.skipIf(x < y, "Pomijamy poniewaz x jest mniejszy od y.")
    def test_sub(self):
        wynik = self.x - self.y
        self.assertEqual(wynik, 4)

    @unittest.skipUnless(y == 0, "Pomijamy ponieważ y jest rowne zero.")
    def test_div(self):
        wynik = self.x / self.y
        self.assertEqual(wynik, 3.0)

    @unittest.expectedFailure
    def test_mul(self):
        wynik = self.x * self.y
        self.assertEqual(wynik, 10)


if __name__ == '__main__':
    unittest.main()