store_name = 'Shopshoe'
item_name = 'Running shoes'
item_price = 100.00
item_discount = 0.30

item_price_discounted = item_price * (1 - item_discount)

print(f'Welcome to {store_name}!')
print('-' * 50)
print(f"Today's special is the {item_name}, which normally costs ${item_price:.2f}.")
print(f"But for a limited time, you can get it for ${item_price_discounted:.2f} ({int(item_discount * 100)}% off)!")
