stock_data = {
    'AAPL': 145.9,
    'GOOG': 2680.7,
    'TSLA': 712.6,
    'AMZN': 3379.1
}

# Enter your solution here

# Enter your solution here
output = ""
with open("208_stock_prices.txt", "w") as f:
    for key, value in stock_data.items():
        name = key
        stock_value = value
        output += f"{name};{stock_value}\n"

    f.writelines(output)