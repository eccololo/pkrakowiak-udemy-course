# {'technology': ['Apple', 'Facebook'], 'gaming': ['Techland', 'EA', 'CD Projekt'], 'finance': ['Berkshire Hathaway', 'Allianz']}


data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

cats = {"technology": [], "gaming": [], "finance": []}

for item in data:
    if item[0] == list(cats.keys())[0]:
        cats["technology"].append(item[1])
    elif item[0] == list(cats.keys())[1]:
        cats["gaming"].append(item[1])
    elif item[0] == list(cats.keys())[2]:
        cats["finance"].append(item[1])

print(cats)