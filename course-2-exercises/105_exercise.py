flights = [
    [
        'United Airlines',
        'UA123',
        'New York',
        'Los Angeles',
        '10:00 AM',
    ],
    [
        'Delta Airlines',
        'DL456',
        'Chicago',
        'Houston',
        '11:30 AM',
    ],
    [
        'American Airlines',
        'AA789',
        'Dallas',
        'San Francisco',
        '08:15 AM',
    ],
    [
        'Southwest Airlines',
        'WN012',
        'Los Angeles',
        'Denver',
        '09:45 AM',
    ],
]

# Enter your solution here

delta_airlines = flights.pop(1)
print(len(flights))
flights.append(delta_airlines)
flights_nums = [
    flights[0][1],
    flights[1][1],
    flights[2][1],
    flights[3][1]
]

print(",".join(flights_nums))