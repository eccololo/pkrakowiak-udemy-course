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

def_dict = defaultdict(list)

for sector, company in data:
    def_dict[sector].append(company)

print(def_dict)