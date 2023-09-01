# [OUT]
# defaultdict(<class 'int'>, {'001': 233, '003': 33, '002': 126})

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


def group_and_sum():
    return "Not Found"


def_dict = defaultdict(int)

for idx in range(len(transactions)):
    key = transactions[idx][0]
    def_dict[key] = 0

for idx in range(len(transactions)):
    value = transactions[idx][1]
    key = transactions[idx][0]
    def_dict[key] += value

print(def_dict)

# Other solution
# def_dict = defaultdict(int)
# for user_id, amount in transactions:
#     def_dict[user_id] += amount
#
# print(def_dict)