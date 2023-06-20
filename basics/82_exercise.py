# [IN]:
# x = 5
# y = 3

# [OUT]:
# The result of the expression1 is: 11
# The result of the expression1 is: 8
# The maximum value in the list is: 9

x = 5
y = 3

expression1 = '2 * 3 + 5'
expression2 = 'x + y'
expression3 = 'max([5, 2, 8, 1, 9, 3])'

print(f"The result of the expression1 is: {eval(expression1)}")
print(f"The result of the expression1 is: {eval(expression2)}")
print(f"The maximum value in the list is: {eval(expression3)}")