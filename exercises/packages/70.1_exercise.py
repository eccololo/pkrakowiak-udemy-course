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

data_dict = {}

for sector, company in data:
    data_dict.setdefault(sector, []).append(company)

print(data_dict)