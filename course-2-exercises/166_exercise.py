cars = [
    {
        'model': 'Sedan',
        'parts': [
            'engine',
            'transmission',
            'chassis',
            'wheels',
        ],
        'cost': 20000,
    },
    {
        'model': 'SUV',
        'parts': [
            'engine',
            'transmission',
            'chassis',
            'wheels',
            'air conditioning',
            'infotainment system',
        ],
        'cost': 35000,
    },
    {
        'model': 'Hatchback',
        'parts': [
            'engine',
            'transmission',
            'chassis',
            'wheels',
            'air conditioning',
        ],
        'cost': 25000,
    },
    {
        'model': 'Pickup Truck',
        'parts': [
            'engine',
            'transmission',
            'chassis',
            'wheels',
            'towing package',
            'bed liner',
        ],
        'cost': 40000,
    },
]

# Enter your solution here
output_dict = {}

for car in cars:
    model = car['model']
    cost = car['cost']
    output_dict[model] = cost

print(output_dict)