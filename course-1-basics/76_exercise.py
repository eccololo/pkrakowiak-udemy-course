# [IN]: {
#     'AAPL': 145.9,
#     'GOOG': 2680.7,
#     'TSLA': 712.6,
#     'AMZN': 3379.1
# }

# [OUT]: 76_stock_prices.txt file:
# AAPL;145.9
# GOOG;2680.7
# TSLA;712.6
# AMZN;3379.1


stock_data = {
    'AAPL': 145.9,
    'GOOG': 2680.7,
    'TSLA': 712.6,
    'AMZN': 3379.1
}

with open("76_stock_prices.txt", "w") as f:
    for key, value in stock_data.items():
        f.write(f"{key};{value}\n")
