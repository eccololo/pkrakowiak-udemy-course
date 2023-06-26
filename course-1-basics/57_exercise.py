products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]

# Enter your solution here
total = 0.9 * sum([item[1] for item in products])

print(f"The total order amount after applying the discount is: {round(total, 1)}")