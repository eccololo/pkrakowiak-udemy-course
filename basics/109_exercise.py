# Załóżmy, że masz listę piłkarzy, gdzie każdy gracz jest reprezentowany przez słownik zawierający nazwisko, pozycję i bramki zdobyte w bieżącym sezonie:
#
#
#
# players = [
#     {'name': 'Alice', 'position': 'Forward', 'goals': 15},
#     {'name': 'Bob', 'position': 'Midfielder', 'goals': 7},
#     {'name': 'Charlie', 'position': 'Defender', 'goals': 2},
#     {'name': 'David', 'position': 'Goalkeeper', 'goals': 0},
#     {'name': 'Eve', 'position': 'Forward', 'goals': 12},
#     {'name': 'Frank', 'position': 'Midfielder', 'goals': 5},
# ]
#
#
# Potrzebujesz stworzyć nowy słownik, który odwzorowuje każdą pozycję na całkowitą liczbę bramek zdobytych przez graczy na tej pozycji. W odpowiedzi wydrukuj otrzymany słownik do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# {'Forward': 27, 'Midfielder': 12, 'Defender': 2, 'Goalkeeper': 0}

players = [
    {'name': 'Alice', 'position': 'Forward', 'goals': 15},
    {'name': 'Bob', 'position': 'Midfielder', 'goals': 7},
    {'name': 'Charlie', 'position': 'Defender', 'goals': 2},
    {'name': 'David', 'position': 'Goalkeeper', 'goals': 0},
    {'name': 'Eve', 'position': 'Forward', 'goals': 12},
    {'name': 'Frank', 'position': 'Midfielder', 'goals': 5},
]

output = {player['position']: sum(item['goals'] for item in players if player['position'] == item['position'])
          for player in players}

print(output)