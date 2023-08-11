places = [
    ('Paris', (48.8566, 2.3522), 100),
    ('London', (51.5072, -0.1276), 120),
    ('Rome', (41.9028, 12.4964), 90),
    ('Barcelona', (41.3851, 2.1734), 80),
    ('Krakow', (50.0647, 19.9450), 60),
    ('Amsterdam', (52.3667, 4.8945), 110),
]

# Enter your solution here
EURUSD = 1.09
output_prices = list(map(lambda x: round(x[2] * EURUSD, 2), places))
print(output_prices)