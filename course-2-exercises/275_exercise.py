import pprint as p

flights = [
    {
        'flight_number': 'ABC123',
        'departure_time': '2023-04-12 08:00',
        'flight_time': 2,
        'departure_city': 'Kraków',
        'arrival_city': 'Warszawa',
    },
    {
        'flight_number': 'DEF456',
        'departure_time': '2023-04-12 10:00',
        'flight_time': 1,
        'departure_city': 'Gdańsk',
        'arrival_city': 'Warszawa',
    },
    {
        'flight_number': 'GHI789',
        'departure_time': '2023-04-12 14:00',
        'flight_time': 3,
        'departure_city': 'Warszawa',
        'arrival_city': 'Kraków',
    },
    {
        'flight_number': 'JKL012',
        'departure_time': '2023-04-12 12:00',
        'flight_time': 2,
        'departure_city': 'Warszawa',
        'arrival_city': 'Gdańsk',
    },
    {
        'flight_number': 'MNO345',
        'departure_time': '2023-04-12 16:00',
        'flight_time': 1,
        'departure_city': 'Kraków',
        'arrival_city': 'Gdańsk',
    },
]

# Enter your solution here

flights_by_arrival_city = {flight['arrival_city']: [
    f for f in flights
    if flight['arrival_city'] == f['arrival_city']
] for flight in flights}
p.pprint(flights_by_arrival_city)