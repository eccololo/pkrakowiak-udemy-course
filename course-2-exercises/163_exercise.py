points = [
    {'player': 'Alice', 'scored': 5},
    {'player': 'Bob', 'scored': 7},
    {'player': 'Charlie', 'scored': 3},
    {'player': 'Alice', 'scored': 2},
    {'player': 'Bob', 'scored': 4},
    {'player': 'Charlie', 'scored': 6},
    {'player': 'Alice', 'scored': 3},
    {'player': 'Bob', 'scored': 8},
    {'player': 'Charlie', 'scored': 1},
]

# Enter your solution here
players_to_points = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

for player in points:
    if player["player"] in players_to_points:
        players_to_points[player['player']] += player['scored']


for player, scored in players_to_points.items():
    print(f"{player} - {scored} points.")
