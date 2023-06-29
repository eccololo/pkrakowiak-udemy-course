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
flight['passengers'][1]['seat'] = '18B'
flight['passengers'].append({'name': 'Bob Johnson', 'seat': '19C', 'meal': 'Halal'})
num_passengers = len(flight['passengers'])

print(f"""From {flight['origin']['city']}, {flight['origin']['state']} ({flight['origin']['airport']})
To {flight['destination']['city']}, {flight['destination']['country']} ({flight['destination']['airport']})
Departure time: {flight['departure_time']}
Arrival time: {flight['arrival_time']}
Number of passengers: {num_passengers}""")