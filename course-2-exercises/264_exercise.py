products = [
    {'id': 1, 'name': 'Keyboard', 'price': 110},
    {'id': 2, 'name': 'Mouse', 'price': 50},
    {'id': 3, 'name': 'Monitor', 'price': 200},
    {'id': 4, 'name': 'Loudspeakers', 'price': 75},
    {'id': 5, 'name': 'Headphones', 'price': 90},
]

# Enter your solution here
avg_price = sum(product['price'] for product in products) / len(products)
output_list = [product for product in products if product['price'] > avg_price]
print(output_list)