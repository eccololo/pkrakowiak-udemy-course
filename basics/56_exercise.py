products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]

# Enter your solution here
total = 0
for item in products:
    total += item[1]
print(f"The total order amount is: {round(total, 1)}")