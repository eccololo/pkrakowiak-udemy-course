item1 = 'Apples'
quantity1 = 5
price1 = 1.50

item2 = 'Bananas'
quantity2 = 7
price2 = 0.99

item3 = 'Oranges'
quantity3 = 4
price3 = 2.25

# Enter your solution here

print("|", "-" * 14, "|", "-" * 13, "|", "-" * 13, sep="-", end="|\n")
print(f"|  {item1:14}| {quantity1:<14}| ${price1:<12}|")
print(f"|  {item2:14}| {quantity2:<14}| ${price2:<12}|")
print(f"|  {item3:14}| {quantity3:<14}| ${price3:<12}|")

# |---------------|---------------|---------------|
# | Apples        | 5             | $1.50         |
# | Bananas       | 7             | $0.99         |
# | Oranges       | 4             | $2.25         |