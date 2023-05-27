category = 'crime'
quantity = 5
book_price = 100.0

# Enter your solution here
rabat = None
if category == "crime":
    if quantity >= 5:
        rabat = 0.2
    elif quantity >= 3:
        rabat = 0.1
    else:
        rabat = 1
elif category == "fantasy":
    if quantity >= 10:
        rabat = 0.25
    elif quantity >= 5:
        rabat = 0.15
    else:
        rabat = 1
else:
    if quantity >= 20:
        rabat = 0.1
    elif quantity >= 10:
        rabat = 0.05
    else:
        rabat = 1

print(f"The total price after the discount is {book_price - round(book_price * rabat, 1)} PLN.")