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
print(f"LeBron James weighs {team['players']['LeBron James']['weight']} kg.")
team['players']['Anthony Davis']['number'] = 23
print(f"Team: Lakers - Anthony Davis ({team['players']['Anthony Davis']['position']}, #{team['players']['Anthony Davis']['number']})")