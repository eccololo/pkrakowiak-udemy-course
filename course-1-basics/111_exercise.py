# [IN]: [(1, 20), (2, 15), (3, 25), (4, 18), (5, 22), (6, 21)]
# [OUT]: {1, 3, 5, 6}

data = [(1, 20), (2, 15), (3, 25), (4, 18), (5, 22), (6, 21)]

# Enter your solution here

output_set = {item[0] for item in data if item[1] >= 20}

print(output_set)