products = ['T-shirt', 'Jeans', 'Sneakers', 'Backpack', 'Watch']
query = 'Sneakers'

# Enter your solution here
for prod in products:
    if prod == query:
        print(f"Product found: {query}")
        break
else:
    print("Product not found")