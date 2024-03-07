import copy


stocks = [['CDR', '11B'], ['PLW'], ['TEN']]

stocks_copied = copy.copy(stocks)
stocks_copied[0][1] = 'CRJ'

print(stocks)
print(stocks_copied)