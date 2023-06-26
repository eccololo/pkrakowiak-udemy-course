# [IN]:  [
#     {'name': 'Alice', 'rank': 'Private', 'service_years': 2},
#     {'name': 'Bob', 'rank': 'Sergeant', 'service_years': 4},
#     {'name': 'Charlie', 'rank': 'Sergeant', 'service_years': 6},
#     {'name': 'David', 'rank': 'Lieutenant', 'service_years': 3},
#     {'name': 'Eve', 'rank': 'Private', 'service_years': 1},
#     {'name': 'Frank', 'rank': 'Lieutenant', 'service_years': 7},
# ]

# [OUT]: {'Private': 2, 'Sergeant': 2, 'Lieutenant': 2}

soldiers = [
    {'name': 'Alice', 'rank': 'Private', 'service_years': 2},
    {'name': 'Bob', 'rank': 'Sergeant', 'service_years': 4},
    {'name': 'Charlie', 'rank': 'Sergeant', 'service_years': 6},
    {'name': 'David', 'rank': 'Lieutenant', 'service_years': 3},
    {'name': 'Eve', 'rank': 'Private', 'service_years': 1},
    {'name': 'Frank', 'rank': 'Lieutenant', 'service_years': 7},
]


# Enter your solution here
output = {'Private': 0, 'Sergeant': 0, 'Lieutenant': 0}
for dict_item in soldiers:
    output[dict_item["rank"]] += 1

print(output)
