def calculate_income_tax(amount, tax_rate, age):
    """
    Calculates the income tax based on the given amount, tax rate,
    and age.

    :param amount: The amount of income.
    :param tax_rate: The tax rate as a decimal.
    :param age: The age of the taxpayer.
    :return: The amount of income tax.
    """
    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))


# Enter your solution here
def test_calculate_income_tax():
    assert calculate_income_tax(60000, 0.15, 10) == 5000

    assert calculate_income_tax(60000, 0.15, 18) == 5000

    assert calculate_income_tax(60000, 0.15, 19) == 9000

    assert calculate_income_tax(60000, 0.15, 65) == 9000

    assert calculate_income_tax(60000, 0.15, 66) == 8000


test_calculate_income_tax()
