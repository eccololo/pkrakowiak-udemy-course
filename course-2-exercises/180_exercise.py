maze = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'W', 'E', 'W', 'W', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'E', 'E', 'W', 'E', 'E', 'W'],
    ['W', 'E', 'W', 'E', 'W', 'E', 'W', 'E', 'W', 'W'],
    ['W', 'E', 'E', 'E', 'W', 'E', 'W', 'E', 'E', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
]

# Enter your solution here

index_pairs = []
for idx_r, row in enumerate(maze):
    for idx_c, col in enumerate(row):
        if col != "E":
            continue
        index_pairs.append([idx_r, idx_c])

print(index_pairs)