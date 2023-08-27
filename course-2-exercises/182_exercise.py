call_records = [
    {
        'name': 'John',
        'phone': '123456789',
        'duration': 30,
        'cost': 5.0,
    },
    {
        'name': 'Jane',
        'phone': '234567890',
        'duration': 90,
        'cost': 10.0,
    },
    {
        'name': 'John',
        'phone': '345678901',
        'duration': 120,
        'cost': 15.0,
    },
    {
        'name': 'Alice',
        'phone': '456789012',
        'duration': 45,
        'cost': 7.5,
    },
    {
        'name': 'John',
        'phone': '567890123',
        'duration': 75,
        'cost': 9.0,
    },
]

caller_name = 'John'
# Enter your solution here
total_call_duration = 0

for call in call_records:
    if call['duration'] < 60:
        continue

    total_call_duration += call['duration'] if call['name'] == "John" else 0

print(f"Total call duration for John, {total_call_duration} seconds")