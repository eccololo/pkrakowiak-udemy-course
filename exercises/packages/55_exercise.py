from collections import ChainMap


stocks_1 = {'CDR': 400, 'PLW': 490}
stocks_2 = {'PLW': 500, 'TEN': 550, 'BBT': 30}

stocks = ChainMap(stocks_1, stocks_2)

print(stocks)