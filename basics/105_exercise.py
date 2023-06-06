# Załóżmy, że masz przeanalizować listę rekordów pacjentów, gdzie każdy rekord jest słownikiem zawierającym informacje o pacjencie, w tym jego imię i nazwisko, wiek oraz odczyty ciśnienia krwi (skurczowego - systolic i rozkurczowego - diastolic):
#
#
#
# patients = [
#     {'name': 'Alice', 'age': 45, 'systolic': 140, 'diastolic': 90},
#     {'name': 'Bob', 'age': 38, 'systolic': 120, 'diastolic': 80},
#     {'name': 'Charlie', 'age': 55, 'systolic': 150, 'diastolic': 95},
#     {'name': 'David', 'age': 62, 'systolic': 130, 'diastolic': 100},
#     {'name': 'Eve', 'age': 29, 'systolic': 135, 'diastolic': 85},
# ]
#
#
# Potrzebujesz utworzyć nową listę zawierającą tylko nazwiska pacjentów z wysokim ciśnieniem krwi, zdefiniowanym jako odczyt skurczowy większy niż 140 i/lub odczyt rozkurczowy większy niż 90. Otrzymaną listę wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# ['Charlie', 'David']

patients = [
    {'name': 'Alice', 'age': 45, 'systolic': 140, 'diastolic': 90},
    {'name': 'Bob', 'age': 38, 'systolic': 120, 'diastolic': 80},
    {'name': 'Charlie', 'age': 55, 'systolic': 150, 'diastolic': 95},
    {'name': 'David', 'age': 62, 'systolic': 130, 'diastolic': 100},
    {'name': 'Eve', 'age': 29, 'systolic': 135, 'diastolic': 85},
]

# Enter your solution here

output = [dict_item["name"] for dict_item in patients if dict_item["systolic"] > 140 or dict_item["diastolic"] > 90]

print(output)
