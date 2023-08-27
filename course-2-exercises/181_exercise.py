enemies = [
    {'name': 'Goblin', 'health': 50, 'damage': 10},
    {'name': 'Orc', 'health': 75, 'damage': 15},
    {'name': 'Troll', 'health': 20, 'damage': 20},
    {'name': 'Dwarf', 'health': 0, 'damage': 15},
    {'name': 'Dragon', 'health': 200, 'damage': 30},
]

player_damage = 25

# Enter your solution here
for enemy in enemies:
    if enemy['health'] <= 0:
        continue
    enemy['health'] -= player_damage
    print(f"You attack the {enemy['name']}")
    if enemy['health'] <= 0:
        print(f'You defeated the {enemy["name"]}')