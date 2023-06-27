stock_prices = [
    102.3,
    103.4,
    105.6,
    108.2,
    109.7,
    112.4,
    113.6,
    115.2,
    116.8,
    119.1,
    121.3,
    122.5,
    124.7,
    126.1,
    127.4,
    129.2,
    130.4,
    132.6,
    133.8,
    135.1,
    136.3,
]

# Enter your solution here
first_avg = sum(stock_prices[:5]) / len(stock_prices[:5])
last_avg = sum(stock_prices[-5:]) / len(stock_prices[-5:])

print(f"Average stock price for the first week: ${first_avg:.2f}")
print(f"Average stock price for the last week: ${last_avg:.2f}")