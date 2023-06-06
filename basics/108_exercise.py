# Załóżmy, że masz listę związków chemicznych, gdzie każdy związek jest reprezentowany przez słownik zawierający jego nazwę i listę atomów tworzących związek:
#
#
#
# compounds = [
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
#
#
# Potrzebujesz stworzyć nowy słownik, który odwzorowuje każdy unikalny atom we wszystkich związkach na całkowitą liczbę wystąpień we wszystkich związkach. Otrzymany słownik wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# {'H': 3, 'O': 2, 'C': 2}


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
