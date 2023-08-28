products = [
    {'id': 1, 'name': 'Keyboard', 'price': 100, 'in_stock': True},
    {'id': 2, 'name': 'Mouse', 'price': 50, 'in_stock': False},
    {'id': 3, 'name': 'Monitor', 'price': 200, 'in_stock': True},
    {'id': 4, 'name': 'Speakers', 'price': 75, 'in_stock': True},
    {'id': 5, 'name': 'Headphones', 'price': 90, 'in_stock': False},
]

# Enter your solution here
output_dict = {product['name']: product['price'] for product in products if product["in_stock"]}
output_dict_sorted = {
    product_name: product_price
    for product_name, product_price in sorted(
        output_dict.items(), key=lambda item: item[1]
    )
}
print(output_dict_sorted)