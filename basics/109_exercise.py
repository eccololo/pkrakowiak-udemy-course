# [IN]:  [
#     {'name': 'Alice', 'position': 'Forward', 'goals': 15},
#     {'name': 'Bob', 'position': 'Midfielder', 'goals': 7},
#     {'name': 'Charlie', 'position': 'Defender', 'goals': 2},
#     {'name': 'David', 'position': 'Goalkeeper', 'goals': 0},
#     {'name': 'Eve', 'position': 'Forward', 'goals': 12},
#     {'name': 'Frank', 'position': 'Midfielder', 'goals': 5},
# ]
# [OUT]: {'Forward': 27, 'Midfielder': 12, 'Defender': 2, 'Goalkeeper': 0}

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