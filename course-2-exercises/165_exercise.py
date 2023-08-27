sales = [
    {'product_id': 1, 'quantity': 3, 'price': 10.99},
    {'product_id': 2, 'quantity': 1, 'price': 34.99},
    {'product_id': 1, 'quantity': 2, 'price': 10.99},
    {'product_id': 3, 'quantity': 5, 'price': 5.99},
    {'product_id': 2, 'quantity': 2, 'price': 34.99},
    {'product_id': 1, 'quantity': 1, 'price': 10.99},
]

# Enter your solution here
sales_raport = {
    1: 0,
    2: 0,
    3: 0
}
unique_products = [1, 2, 3]

for sale in sales:
    if sale['product_id'] in unique_products:
        revenue = round(sale['quantity'] * sale['price'], 2)
        sales_raport[sale['product_id']] += revenue


for sale_prod, sale_rep_value in sales_raport.items():
    print(f"Product {sale_prod} generated ${sale_rep_value} in revenue")