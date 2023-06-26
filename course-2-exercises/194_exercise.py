# [IN]: fill_value(height=2, width=3, value=255)
# [OUT]: [[255, 255, 255], [255, 255, 255]]
#
#
# [IN]: fill_value(4, 2, 'a')
# [OUT]: [['a', 'a'], ['a', 'a'], ['a', 'a'], ['a', 'a']]

def fill_value(height, width, value):
    output_array = []
    partial_array = []

    for _ in range(height):
        partial_array = []
        for _ in range(width):
            partial_array.append(value)
        output_array.append(partial_array)

    return output_array


print(fill_value(4, 2, "a"))
