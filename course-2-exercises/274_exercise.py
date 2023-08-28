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
flight_numbers = []
flights_by_arrival_city = {flight['arrival_city']: [f['flight_number']
                                                    for f in flights
                                                    if f['arrival_city'] == flight['arrival_city']]
                           for flight in flights}
print(flights_by_arrival_city)
