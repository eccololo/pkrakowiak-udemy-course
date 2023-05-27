stocks = {"AMZN.US": "Amazon.com Inc", "GOOGL.US": "Alphabet Inc",
          "AAPL.US": "Apple Inc", "UBER.US": "Uber Technologies Inc",
          "MSFT.US": "Microsoft Corp"}

print(stocks.keys())
print(stocks.values())
print(stocks.items())

for key, value in stocks.items():
    print("{:8}: {}".format(key, value))

# Dict Comprehension
result = {key: value for (key, value) in stocks.items()}
print(result)

stocks_set = {(key, value) for (key, value) in stocks.items()}
print(type(stocks_set))
print(stocks_set)

# Reverse dict with unique value
stocks_reversed = {value: key for (key, value) in stocks.items()}
print(stocks_reversed)

stocks_lower = {key.lower(): value for (key, value) in stocks.items()}
print(stocks_lower)

result_len = {key: len(value) for (key, value) in stocks.items()}
print(result_len)

result_len_2 = {key: value + ":" + str(len(value)) for (key, value) in stocks.items()}
print(result_len_2)


def replace_corp_inc(name):
    name = name.replace("Corp", "0")
    name = name.replace("Inc", "1")
    return name


stocks_flag = {key: replace_corp_inc(value) for (key, value) in stocks.items()}
print(stocks_flag)

stocks_if = {key: val for (key, val) in stocks.items() if "Corp" in val}
print(stocks_if)

stocks_A = {key: value for (key, value) in stocks.items()
            if value.startswith("A") if len(value) < 13}
print(stocks_A)
