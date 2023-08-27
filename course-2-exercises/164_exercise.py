import math

# [OUT]:
# liczbę lotów opóźnionych
# średni czas opóźnienia lotu


flights = [
    {
        'flight_num': 'AA123',
        'origin': 'LAX',
        'destination': 'JFK',
        'delay_minutes': 12,
    },
    {
        'flight_num': 'BB456',
        'origin': 'ORD',
        'destination': 'LAX',
        'delay_minutes': 0,
    },
    {
        'flight_num': 'CC789',
        'origin': 'JFK',
        'destination': 'ORD',
        'delay_minutes': 32,
    },
    {
        'flight_num': 'AA321',
        'origin': 'LAX',
        'destination': 'ORD',
        'delay_minutes': 6,
    },
    {
        'flight_num': 'BB654',
        'origin': 'JFK',
        'destination': 'LAX',
        'delay_minutes': 18,
    },
    {
        'flight_num': 'CC987',
        'origin': 'ORD',
        'destination': 'JFK',
        'delay_minutes': 24,
    },
]

# Enter your solution here
delayed_flights = 0
total_delayed_mins = 0

for flight in flights:
    if flight["delay_minutes"] > 0:
        delayed_flights += 1
        total_delayed_mins += flight["delay_minutes"]

print(f"Total number of delayed flights: {delayed_flights}")
print(f"Average delay time: {total_delayed_mins / delayed_flights:.2f} minutes")