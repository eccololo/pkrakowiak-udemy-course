orders = [
    {'id': 1, 'product': 'laptop', 'status': 'processing'},
    {'id': 2, 'product': 'smartphone', 'status': 'shipped'},
    {'id': 3, 'product': 'tablet', 'status': 'processing'},
    {'id': 4, 'product': 'headphones', 'status': 'processing'},
    {'id': 5, 'product': 'monitor', 'status': 'shipped'},
]

# Enter your solution here
output_list = list(filter(lambda x: x['status'] == 'processing', orders))
for item in output_list:
    print(item)