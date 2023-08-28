products = [
    {
        'name': 'T-shirt',
        'color': 'white',
        'sizes': ['S', 'M', 'L', 'XL'],
    },
    {
        'name': 'Trousers',
        'color': 'blue',
        'sizes': ['M', 'L', 'XL'],
    },
    {
        'name': 'Jacket',
        'color': 'black',
        'sizes': ['L', 'XL', 'XXL'],
    },
    {
        'name': 'Shoes',
        'color': 'red',
        'sizes': ['40', '41', '42', '43', '44'],
    },
]

# Enter your solution here
unique_combinations = {f"{product['color']} - {size}"
                       for product in products
                       for size in product['sizes']}
print(unique_combinations)