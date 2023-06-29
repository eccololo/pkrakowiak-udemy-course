team = {
    'name': 'Lakers',
    'city': 'Los Angeles',
    'players': {
        'LeBron James': {
            'position': 'Forward',
            'number': 23,
            'height': 203,
            'weight': 113,
        },
        'Anthony Davis': {
            'position': 'Center',
            'number': 3,
            'height': 208,
            'weight': 115,
        },
        'Russell Westbrook': {
            'position': 'Guard',
            'number': 0,
            'height': 190,
            'weight': 91,
        },
    },
}

# Enter your solution here
team['players']['Kobe Bryant'] = {
    'position': 'Guard',
    'number': 24,
    'height': 198,
    'weight': 96,
}

print(len(team['players']))
print(team['players']['Kobe Bryant']['number'])