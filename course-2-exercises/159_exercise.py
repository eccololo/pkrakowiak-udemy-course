cities = ['Paris', 'Rome', 'Barcelona', 'Berlin']

flight_prices = {
    'Paris': 350,
    'Rome': 450,
    'Barcelona': 300,
    'Amsterdam': 250,
    'Berlin': 400
}

# Enter your solution here
total_cost = 0
for key, value in flight_prices.items():
    if key in cities:
        total_cost += value

print(f"Total cost of flights: $ {total_cost}.")