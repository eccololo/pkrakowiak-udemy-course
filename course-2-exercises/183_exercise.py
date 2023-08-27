construction_tasks = [
    {
        'name': 'Foundation',
        'description': 'Excavate and pour concrete',
        'completed': True,
    },
    {
        'name': 'Framing',
        'description': 'Frame the walls, roof, and floors',
        'completed': False,
    },
    {
        'name': 'Plumbing',
        'description': 'Install the plumbing and fixtures',
        'completed': False,
    },
    {
        'name': 'Electrical',
        'description': 'Install the electrical wiring and outlets',
        'completed': True,
    },
    {
        'name': 'Drywall',
        'description': 'Install drywall on the walls and ceilings',
        'completed': False,
    },
]

# Enter your solution here

for task in construction_tasks:
    if task['completed']:
        continue
    print(f"{task['name']} is incomplete")