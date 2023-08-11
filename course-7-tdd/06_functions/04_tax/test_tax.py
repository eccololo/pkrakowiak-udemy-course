import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_ten_percent(self):
        self.assertEqual(100, calc_tax(1000, 0.1))

    def test_calc_tax_with_forteen_percent(self):
        self.assertEqual(140, calc_tax(1000, 0.14))

    def test_calc_tax_with_forteen_percent_with_almost_equal(self):
        self.assertAlmostEqual(140, calc_tax(1000, 0.14))

    def test_calc_tax_with_incorrect_amount_type_should_rise_error(self):
        self.assertRaises(TypeError, calc_tax, "ten", 0.14)

    def test_calc_tax_with_incorrect_tax_rate_type_should_rise_error(self):
        self.assertRaises(TypeError, calc_tax, 1000, "0.14")

    def test_calc_tax_with_incorrect_tax_rate_should_rise_error(self):
        self.assertRaises(ValueError, calc_tax, 1000, 1.0)
        self.assertRaises(ValueError, calc_tax, 1000, 0.0)

    def test_calc_tax_with_incorrect_negative_amount_should_rise_error(self):
        self.assertRaises(ValueError, calc_tax, -1000, 0.23)


if __name__ == "__main__":
    unittest.main(verbosity=2)
