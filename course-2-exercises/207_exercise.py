products = [
    {'name': 'T-shirt', 'price': 29.99},
    {'name': 'Shoes', 'price': 99.99},
    {'name': 'Pants', 'price': 49.99},
]

# Enter your solution here
output = ""
with open("207_products.txt", "w") as f:
    for item in products:
        name = item['name']
        price = item['price']
        output += f"{name}, {price}\n"

    f.writelines(output)
