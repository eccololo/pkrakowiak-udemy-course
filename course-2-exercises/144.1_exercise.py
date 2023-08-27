income = 45000.0
marital_status = 'married'

# Enter your solution here
tax_rate = None

if income <= 10000:
    if marital_status == "single":
        tax_rate = 0.1
    else:
        tax_rate = 0.08
elif 50000 >= income > 10001:
    if marital_status == "single":
        tax_rate = 0.15
    else:
        tax_rate = 0.13
elif income > 50001:
    if marital_status == "single":
        tax_rate = 0.2
    else:
        tax_rate = 0.18

print(f"The tax rate is {tax_rate * 100}%.")