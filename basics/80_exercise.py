# [IN]: [-5, 2, 8, -1, 9, -3]
# [OUT]: [-1, 2, -3, -5, 8, 9]

values = [-5, 2, 8, -1, 9, -3]
values = sorted(values, key=lambda x: abs(x))
print(values)