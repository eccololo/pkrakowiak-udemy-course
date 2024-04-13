from collections import defaultdict


transactions = [
    ('001', 100),
    ('003', 10),
    ('002', 80),
    ('001', 90),
    ('002', 46),
    ('001', 43),
    ('003', 23),
]

def_dict = defaultdict(int)

for user_id, amount in transactions:
    def_dict[user_id] += amount

print(def_dict)