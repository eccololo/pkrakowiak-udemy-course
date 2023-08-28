foods = [
    {
        'name': 'buckwheat',
        'gluten_free': True,
        'vegan': True,
        'calories': 90,
    },
    {
        'name': 'bulgur',
        'gluten_free': True,
        'vegan': True,
        'calories': 120,
    },
    {
        'name': 'natural yogurt',
        'gluten_free': True,
        'vegan': False,
        'calories': 70,
    },
    {
        'name': 'cashew nuts',
        'gluten_free': True,
        'vegan': True,
        'calories': 150,
    },
    {
        'name': 'cottage cheese',
        'gluten_free': False,
        'vegan': False,
        'calories': 80,
    },
    {
        'name': 'tofu',
        'gluten_free': True,
        'vegan': True,
        'calories': 70,
    },
    {
        'name': 'rice',
        'gluten_free': True,
        'vegan': True,
        'calories': 130,
    },
    {
        'name': 'wheat bread',
        'gluten_free': False,
        'vegan': True,
        'calories': 150,
    },
]


# Enter your solution here
output_list = list(filter(lambda x: x['gluten_free'] and
                          x['vegan'] and
                          x['calories'] < 100, foods))

for item in output_list:
    print(item)