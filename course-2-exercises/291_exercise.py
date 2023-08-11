net_prices = [
    (100, 'Europe'),
    (120, 'Asia'),
    (80, 'North America'),
    (90, 'South America'),
]
taxes = {
    'Europe': 0.23,
    'Asia': 0.2,
    'North America': 0.18,
    'South America': 0.15,
}


def calculate_gross_price(sale_region, taxes):
    # Enter your solution here
    net_price = sale_region[0]
    region_1 = sale_region[1]
    tax = taxes[region_1]
    price_total = round(net_price * (1 + tax), 1)

    return price_total, region_1


gross_prices = list(
    map(lambda x: calculate_gross_price(x, taxes), net_prices)
)
print(gross_prices)
