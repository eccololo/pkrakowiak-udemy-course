from pathlib import Path


path = Path.home() / 'reports/2020/01/sales.csv'
path_parents = path.parents

for item in path_parents:
    print(item)