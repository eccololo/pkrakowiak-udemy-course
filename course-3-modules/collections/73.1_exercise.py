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

def_dict = defaultdict(set)

for sector, company in data:
    def_dict[sector].add(company)

print(def_dict)