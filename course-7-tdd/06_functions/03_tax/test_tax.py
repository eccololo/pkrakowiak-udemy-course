import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_ten_percent(self):
        self.assertEqual(100, calc_tax(1000, 10))

    def test_calc_tax_with_forteen_percent(self):
        self.assertEqual(140, calc_tax(1000, 14))

    def test_calc_tax_with_forteen_percent_with_almost_equal(self):
        self.assertAlmostEqual(140, calc_tax(1000, 14))


if __name__ == "__main__":
    unittest.main(verbosity=2)
