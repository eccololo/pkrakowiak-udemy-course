from collections import defaultdict


data = [
    ('technology', 'Facebook'),
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

d = defaultdict(set)

for sector, company in data:
    d[sector].add(company)

print(d)