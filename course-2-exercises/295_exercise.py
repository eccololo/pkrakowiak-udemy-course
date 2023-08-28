products = [
    {
        'id': 1,
        'name': 'laptop',
        'category': 'computers',
        'price': 2000,
        'in_stock': True,
    },
    {
        'id': 2,
        'name': 'smartphone',
        'category': 'electronics',
        'price': 1000,
        'in_stock': True,
    },
    {
        'id': 3,
        'name': 'book',
        'category': 'books',
        'price': 50,
        'in_stock': False,
    },
    {
        'id': 4,
        'name': 'monitor',
        'category': 'computers',
        'price': 500,
        'in_stock': True,
    },
    {
        'id': 5,
        'name': 'headphones',
        'category': 'electronics',
        'price': 100,
        'in_stock': False,
    },
]


# Enter your solution here
output_list = list(filter(lambda x:
                          x['price'] >= 500 and
                          x['category'] == "computers" and
                          x['in_stock'], products))

for item in output_list:
    print(item)