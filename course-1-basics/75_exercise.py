# [IN]: [
#     {'name': 'T-shirt', 'price': 29.99},
#     {'name': 'Shoes', 'price': 99.99},
#     {'name': 'Pants', 'price': 49.99},
# ]

# [OUT]: 75_products.txt file:
# T-shirt, 29.99
# Shoes, 99.99
# Pants, 49.99

products = [
    {'name': 'T-shirt', 'price': 29.99},
    {'name': 'Shoes', 'price': 99.99},
    {'name': 'Pants', 'price': 49.99},
]

with open("75_products.txt", "w") as f:
    for item in products:
        name = item["name"]
        price = item["price"]
        f.write(f"{name}, {price}\n")
