def flatten(items):
    output_list = []
    for item in items:
        for x in item:
            output_list.append(x)

    return output_list


items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(flatten(items))