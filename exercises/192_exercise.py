def concat(lista1, lista2):
    output_list = []
    for item in zip(lista1, lista2):
        step_list = item[0] + item[1]
        output_list.append(step_list)

    return output_list


l1 = [[1], [2]]
l2 = [[3], [4]]

print(concat(l1, l2))