# [IN]: [
#     {'name': 'Alice', 'age': 45, 'systolic': 140, 'diastolic': 90},
#     {'name': 'Bob', 'age': 38, 'systolic': 120, 'diastolic': 80},
#     {'name': 'Charlie', 'age': 55, 'systolic': 150, 'diastolic': 95},
#     {'name': 'David', 'age': 62, 'systolic': 130, 'diastolic': 100},
#     {'name': 'Eve', 'age': 29, 'systolic': 135, 'diastolic': 85},
# ]

# [OUT]: ['Charlie', 'David']

patients = [
    {'name': 'Alice', 'age': 45, 'systolic': 140, 'diastolic': 90},
    {'name': 'Bob', 'age': 38, 'systolic': 120, 'diastolic': 80},
    {'name': 'Charlie', 'age': 55, 'systolic': 150, 'diastolic': 95},
    {'name': 'David', 'age': 62, 'systolic': 130, 'diastolic': 100},
    {'name': 'Eve', 'age': 29, 'systolic': 135, 'diastolic': 85},
]

# Enter your solution here

output = [dict_item["name"] for dict_item in patients if dict_item["systolic"] > 140 or dict_item["diastolic"] > 90]

print(output)
