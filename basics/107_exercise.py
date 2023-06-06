# Załóżmy, że masz listę żołnierzy w jednostce wojskowej, gdzie każdy żołnierz jest reprezentowany przez słownik zawierający nazwisko, stopień i lata służby:
#
#
#
# soldiers = [
#     {'name': 'Alice', 'rank': 'Private', 'service_years': 2},
#     {'name': 'Bob', 'rank': 'Sergeant', 'service_years': 4},
#     {'name': 'Charlie', 'rank': 'Sergeant', 'service_years': 6},
#     {'name': 'David', 'rank': 'Lieutenant', 'service_years': 3},
#     {'name': 'Eve', 'rank': 'Private', 'service_years': 1},
#     {'name': 'Frank', 'rank': 'Lieutenant', 'service_years': 7},
# ]
#
#
# Chcesz stworzyć nowy słownik, który odwzorowuje każdą rangę na całkowitą liczbę żołnierzy w jednostce, którzy posiadają daną rangę (klucz rank). Otrzymaną listę wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# {'Private': 2, 'Sergeant': 2, 'Lieutenant': 2}

soldiers = [
    {'name': 'Alice', 'rank': 'Private', 'service_years': 2},
    {'name': 'Bob', 'rank': 'Sergeant', 'service_years': 4},
    {'name': 'Charlie', 'rank': 'Sergeant', 'service_years': 6},
    {'name': 'David', 'rank': 'Lieutenant', 'service_years': 3},
    {'name': 'Eve', 'rank': 'Private', 'service_years': 1},
    {'name': 'Frank', 'rank': 'Lieutenant', 'service_years': 7},
]


# Enter your solution here
output = {'Private': 0, 'Sergeant': 0, 'Lieutenant': 0}
for dict_item in soldiers:
    output[dict_item["rank"]] += 1

print(output)
