parts = [
    ['50x20x1.5', '25x10x1.0'],
    ['55x22x1.8', '30x15x1.2'],
    ['60x24x2.0', '35x20x1.5'],
]

# Enter your solution here
dimensions = parts[1][0]
length = float(dimensions[:2])
width = float(dimensions[3:5])
heigth = float(dimensions[-3:])

print(f"length = {length}")
print(f"width = {width}")
print(f"height = {heigth}")