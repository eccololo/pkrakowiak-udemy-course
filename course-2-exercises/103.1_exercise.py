menu = [
    [
        'Spaghetti Bolognese',
        12.99,
        [
            'spaghetti',
            'tomato sauce',
            'ground beef',
            'onion',
        ],
    ],
    [
        'Caesar Salad',
        8.99,
        [
            'romaine lettuce',
            'croutons',
            'parmesan cheese',
            'Caesar dressing',
        ],
    ],
    [
        'Margherita Pizza',
        14.99,
        [
            'pizza dough',
            'tomato sauce',
            'mozzarella cheese',
            'basil',
        ],
    ],
]

# Enter your solution here

menu[1][2].append('olive oil')
menu[1][1] = 9.99

print(menu[1])