airports = [
    (
        'JFK',
        'John F. Kennedy International Airport',
        (40.6413, -73.7781),
        3,
    ),
    (
        'EWR',
        'Newark Liberty International Airport',
        (40.6895, -74.1745),
        6,
    ),
    (
        'LAX',
        'Los Angeles International Airport',
        (33.9416, -118.4085),
        38,
    ),
    (
        'SFO',
        'San Francisco International Airport',
        (37.6213, -122.3790),
        4,
    ),
    (
        'ORD',
        'Chicago O\'Hare International Airport',
        (41.9742, -87.9073),
        204,
    ),
]

# Enter your solution here

output = sorted(list(map(lambda x: x[0], airports)))
print(output)