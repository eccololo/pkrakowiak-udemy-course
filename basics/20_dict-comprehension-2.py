stocks = {"AMZN.US": "Amazon.com Inc", 
"GOOGL.US": "Alphabet Inc", "AAPL.US": "Apple Inc",
"UBER.US": "Uber Technologies Inc", 
"MSFT.US": "Microsoft Corp"}

stocks_if = {key: "Corp" if "Corp" in val else "Inc" for (key, val) in stocks.items()}
print(stocks_if)


# 6 linijek kodu
numbers = range(20)
numbers_dict = {}
for n in numbers:
    if n % 2 == 0:
        numbers_dict[n] = n ** 2
print(numbers_dict)

# 1 linijka kodu
numbers_dict = {key: key ** 2 for key in numbers if key % 2 == 0}
print(numbers_dict)

nested_dict = {
    '001': {'price': 100},
    '002': {'price': 60},
    '003': {'price': 80}
}

nested_dict_price = {key: val['price'] for (key, val) in nested_dict.items()}
print(nested_dict_price)

nested_dict = {
    '001': {'price': 100, 'items': 5},
    '002': {'price': 60, 'items': 7},
    '003': {'price': 80, 'items': 10}
}

nested_dict_values = {key: value['price'] * value['items'] for (key, value) in nested_dict.items()}
print(nested_dict_values)
