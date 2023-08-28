processors = [
    {'model': 'Intel Core i5-11600K', 'cores': 6},
    {'model': 'AMD Ryzen 5 5600X', 'cores': 6},
    {'model': 'Intel Core i9-11900K', 'cores': 8},
    {'model': 'AMD Ryzen 9 5900X', 'cores': 12},
    {'model': 'Intel Xeon W-3175X', 'cores': 28},
]

# Enter your solution here

output_list = list(filter(lambda x: x['cores'] > 8, processors))
for item in output_list:
    print(item)