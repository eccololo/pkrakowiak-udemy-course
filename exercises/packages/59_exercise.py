from collections import ChainMap


techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance = {'Citigroup': 51, 'Allianz': 180}
gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

stocks = ChainMap(techs, finance, gaming)

print(sorted(stocks.keys()))