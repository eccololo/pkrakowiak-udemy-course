# [IN]: multiply(4, 2)
# [OUT]: 8
#
# [IN]: multiply(4, 3, 2)
# [OUT]: 24
#
# [IN]: multiply(4, 3, 2)
# [OUT]: None

def multiply(*args):
    if len(args) == 0:
        return None
    output = 1
    for i in args:
        output *= i
    return output


print(multiply(4, 2))
print(multiply(4, 3, 2))
