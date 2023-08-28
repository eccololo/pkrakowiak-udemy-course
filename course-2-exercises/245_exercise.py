def order_number_generator(prefix, start, end):
    # Enter your solution here
    for i in range(start, end):
        yield prefix + "-" + str(i).zfill(6)


for order_num in order_number_generator('ORD', 100, 110):
    print(order_num)

print()

for order_num in order_number_generator('#111', 10, 20):
    print(order_num)