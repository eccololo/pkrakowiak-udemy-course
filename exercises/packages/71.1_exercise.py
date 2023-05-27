# {'technology': ['Apple', 'Facebook'], 'gaming': ['Techland', 'EA', 'CD Projekt'], 'finance': ['Berkshire Hathaway', 'Allianz']})

from collections import defaultdict


data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

d = defaultdict(list)
for sector, company in data:
    d[sector].append(company)

print(d)