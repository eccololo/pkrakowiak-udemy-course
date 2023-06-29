flight = {
    'airline': 'Delta',
    'flight_number': 'DL215',
    'origin': {
        'airport': 'JFK',
        'city': 'New York',
        'state': 'NY',
        'country': 'USA',
    },
    'destination': {
        'airport': 'LHR',
        'city': 'London',
        'country': 'UK',
    },
    'departure_time': '2023-05-01T08:00:00Z',
    'arrival_time': '2023-05-01T20:00:00Z',
    'passengers': [
        {'name': 'John Smith', 'seat': '17A', 'meal': 'Vegetarian'},
        {'name': 'Jane Doe', 'seat': '17B', 'meal': 'Kosher'},
    ],
}

# Enter your solution here

airline = flight['airline']
origin_airport = flight['origin']['airport']
num_passengers = len(flight['passengers'])
flight_number = flight['flight_number']

print(f"""Airline: {airline}
Origin airport code: {origin_airport}
Flight: {flight_number}
Number of passengers: {num_passengers}""")