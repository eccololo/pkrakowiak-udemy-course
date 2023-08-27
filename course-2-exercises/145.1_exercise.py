current_price = 75.0
price_trend = 'up'
average_price = 70.0

# Enter your solution here

action = None

if price_trend == "up":
    if current_price <= average_price:
        action = "hold"
    elif current_price > average_price:
        action = "buy"
elif price_trend == "down":
    if current_price < average_price:
        action = "sell"
    elif current_price >= average_price:
        action = "buy"
elif price_trend == "stable":
    if current_price > average_price:
        action = "sell"


print(f"The recommended action is to {action} the stock.")