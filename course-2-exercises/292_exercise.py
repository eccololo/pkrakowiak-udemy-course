inch_lengths = [2.5, 3.5, 1.8, 2.5, 3.5]

# Enter your solution here
INCH2CM = 2.54

output_cm = list(map(lambda x: x * INCH2CM, inch_lengths))

print(output_cm)