# {'technology': ['Apple', 'Facebook'], 'gaming': ['Techland', 'EA', 'CD Projekt'], 'finance': ['Berkshire Hathaway', 'Allianz']})

from collections import defaultdict


def def_value(data):
    d = {}
    for sector, company in data:
        d.setdefault(sector, []).append(company)

    return d


data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

d = defaultdict(def_value)

print(d["abc"])
