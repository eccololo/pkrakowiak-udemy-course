from functools import reduce

orders = [
    {
        'items': [
            ('Product 1', 10.99),
            ('Product 2', 20.99),
            ('Product 3', 5.99),
        ],
        'shipping': 5.0,
    },
    {
        'items': [
            ('Product 4', 15.99),
            ('Product 5', 8.99)
        ],
        'shipping': 7.5,
    },
    {
        'items': [
            ('Product 6', 12.99),
            ('Product 7', 9.99),
            ('Product 8', 14.99),
        ],
        'shipping': 10.0,
    },
]


# Enter your solution here

def order_revenue(order):
    items_total = sum(item[1] for item in order['items'])
    return items_total + order['shipping']


revenue = reduce(lambda total, order: total + order_revenue(order), orders, 0)
print(f"Total revenue: {revenue}")
