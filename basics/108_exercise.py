# [IN]:  [
#     {
#         'name': 'Water',
#         'atoms': ['H', 'O', 'H'],
#     },
#     {
#         'name': 'Methane',
#         'atoms': ['C', 'H', 'H', 'H', 'H'],
#     },
#     {
#         'name': 'Ethanol',
#         'atoms': ['C', 'H', 'O', 'H', 'H', 'C', 'H', 'H', 'H'],
#     },
# ]

# [OUT]: {'H': 3, 'O': 2, 'C': 2}


compounds = [
    {
        'name': 'Water',
        'atoms': ['H', 'O', 'H'],
    },
    {
        'name': 'Methane',
        'atoms': ['C', 'H', 'H', 'H', 'H'],
    },
    {
        'name': 'Ethanol',
        'atoms': ['C', 'H', 'O', 'H', 'H', 'C', 'H', 'H', 'H'],
    },
]

# Enter your solution here

output = {atom: sum(1 for c in compounds if atom in c["atoms"])
          for compound in compounds
          for atom in compound["atoms"]}

print(output)
