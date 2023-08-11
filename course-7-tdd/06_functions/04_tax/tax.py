def calc_tax(amount, tax_rate):

    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be int or float.")
    if not amount >= 0:
        raise ValueError("Amount must be positive or 0.")

    if not isinstance(tax_rate, float):
        raise TypeError("Amount must be int or float.")
    if not 1 > tax_rate > 0:
        raise ValueError("Tax rate must be greater than 0 and less than 1.")

    return amount * tax_rate