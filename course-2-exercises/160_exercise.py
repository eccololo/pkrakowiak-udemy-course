soldiers = ['John', 'Mike', 'Sarah', 'Kim', 'Tom']

rankings = {
    'John': 'Captain',
    'Mike': 'Private',
    'Kim': 'Lieutenant',
    'Tom': 'Major'
}

# Enter your solution here
for name in soldiers:
    try:
        print(f"{name} is a {rankings[name]}")
    except:
        print(f"{name} has no ranking")