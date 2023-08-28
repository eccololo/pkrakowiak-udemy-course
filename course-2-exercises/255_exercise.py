products = [
    {
        'id': 1,
        'name': 'Keyboard',
        'tags': ['electronics', 'computer accessories'],
    },
    {
        'id': 2,
        'name': 'Mouse',
        'tags': ['electronics', 'computer accessories'],
    },
    {
        'id': 3,
        'name': 'Monitor',
        'tags': ['electronics', 'monitors'],
    },
    {
        'id': 4,
        'name': 'Speakers',
        'tags': ['electronics', 'audio accessories'],
    },
    {
        'id': 5,
        'name': 'Headphones',
        'tags': ['electronics', 'audio accessories'],
    },
]

# Enter your solution here

unique_tags = {tag for product in products for tag in product['tags']}
print(unique_tags)