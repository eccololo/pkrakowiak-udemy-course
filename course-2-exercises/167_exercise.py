maze = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', '_', '_', '_', '_', '_', '_', '_', '_', 'X'],
    ['X', '_', 'X', 'X', 'X', '_', 'X', 'X', '_', 'X'],
    ['X', '_', '_', '_', 'X', '_', '_', '_', '_', 'X'],
    ['X', 'X', 'X', '_', 'X', '_', 'X', 'X', '_', 'X'],
    ['X', '_', '_', '_', 'X', '_', '_', 'X', '_', 'X'],
    ['X', '_', 'X', '_', '_', '_', 'X', 'X', '_', 'X'],
    ['X', '_', 'X', 'X', 'X', '_', '_', '_', '_', 'X'],
    ['X', '_', '_', '_', '_', '_', 'X', '_', '_', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
]

# Enter your solution here
walls = 0
floors = 0

for segment in maze:
    for item in segment:
        if item == "X":
            walls += 1
        else:
            floors += 1

print(f"Floor = {floors}")
print(f"Wall = {walls}")