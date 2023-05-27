cars = [
    {'model': 'Tesla', 'mileage': 15000, 'battery_level': 100},
    {'model': 'Nissan', 'mileage': 30000, 'battery_level': 75},
    {'model': 'BMW', 'mileage': 5000, 'battery_level': 100},
    {'model': 'Ford', 'mileage': 20000, 'battery_level': 50}
]

# Enter your solution here
for car in cars:
    if car["battery_level"] == 100:
        print("The first car with a full charge is:", car["model"])
        break