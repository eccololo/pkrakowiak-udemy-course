import copy


original_data = {
    'name': 'John',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'zip': '12345'
    },
    'hobbies': ['reading', 'coding', 'swimming']
}

deep_copy_data = copy.deepcopy(original_data)

print(deep_copy_data['address'])