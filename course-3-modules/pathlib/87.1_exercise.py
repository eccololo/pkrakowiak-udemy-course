from pathlib import Path

path1 = Path(f"{Path.home()}/reports/2020/01/sales.csv")
path2 = Path(f"{Path.cwd()}/reports/2020/01/sales.csv")

print(path1)
print(path2)