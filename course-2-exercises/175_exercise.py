taxi_drivers = [
    ('John', 4.2),
    ('Jane', 4.45),
    ('Bob', 4.3),
    ('Alice', 4.8),
    ('Mike', 3.9),
]

# Enter your solution here

for taxi_driver in taxi_drivers:
    if taxi_driver[1] >= 4.5:
        print(f"Suitable driver found: {taxi_driver[0]}")
        break
else:
    print("No suitable driver found.")