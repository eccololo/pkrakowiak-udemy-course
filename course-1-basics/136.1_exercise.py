item1_price = 100.0
item2_price = 50.0
discount_code = 'DISCOUNT20'
discount = None
total_price = None
# Enter your solution here

if discount_code == "DISCOUNT10":
    discount = 0.1
    total_price = (item1_price + item2_price) * (1 - discount)
    print(f"Total price of the order is $ {total_price}")
elif discount_code == "DISCOUNT20":
    discount = 0.2
    total_price = (item1_price + item2_price) * (1 - discount)
    print(f"Total price of the order is $ {total_price}")
else:
    print("Info: Invalid discount code. No discount will be applied.")