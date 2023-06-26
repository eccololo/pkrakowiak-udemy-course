products = [
    ('T-shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 100.00),
    ('Shoes', 'Footwear', 150.00)
]

# Enter your solution here

for item in products:
    if item[1] == "Clothing":
        # print(item)
        print(item[0], item[2])