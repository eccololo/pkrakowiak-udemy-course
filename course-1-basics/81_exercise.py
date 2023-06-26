# [IN]:
# 5
# 'Hello, world!'
# [5, 2, 8, 1, 9, 3]

# [OUT]:
# The number is of type int.
# The string is of type str.
# The object is of type list.

number = 5
string = 'Hello, world!'
values = [5, 2, 8, 1, 9, 3]

if type(number) == int:
    print('The number is of type int.')
elif type(number) == float:
    print('The number is of type float.')

if type(string) == str:
    print('The string is of type str.')

if type(values) == tuple:
    print('The object is of type tuple.')
elif type(values) == list:
    print('The object is of type list.')