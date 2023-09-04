from pathlib import Path

cwd_dir = Path.cwd()
home_dir = Path.home()

path1 = Path(f"{cwd_dir}/reports/2020/01/sales.csv")
path2 = Path(f"{home_dir}/reports/2020/01/sales.csv")

print(path1)
print(path2)