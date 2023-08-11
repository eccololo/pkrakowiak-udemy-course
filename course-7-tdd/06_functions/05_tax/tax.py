def calc_tax(amount, tax_rate, age):
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be int or float.")
    if not amount >= 0:
        raise ValueError("Amount must be positive or 0.")

    if not isinstance(tax_rate, float):
        raise TypeError("Amount must be int or float.")
    if not 1 > tax_rate > 0:
        raise ValueError("Tax rate must be greater than 0 and less than 1.")

    if not isinstance(age, int):
        raise TypeError("Age must be int.")
    if not age > 0:
        raise ValueError("Age must be greater than 0.")

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))
