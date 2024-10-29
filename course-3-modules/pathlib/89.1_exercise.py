from pathlib import Path


path = Path.home() / 'reports/2020/01/sales.csv'

# print(path.parent)

for part in path.parents:
    print(part)