import copy


stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.deepcopy(stocks)

stocks_copied[0][1] = 'CRJ'

print("stocks:", stocks)
print("stocks_copied:", stocks_copied)