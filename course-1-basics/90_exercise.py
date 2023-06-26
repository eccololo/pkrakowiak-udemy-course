# [IN]: ['Warsaw', 'London', 'Berlin', 'New York']

# [OUT]: ['War', 'Lon', 'Ber', 'New']

cities = ['Warsaw', 'London', 'Berlin', 'New York']

output = list(map(lambda x: x[:3], cities))
print(output)