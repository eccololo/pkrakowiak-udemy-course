from pathlib import Path
from pprint import pprint


paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'
    for i in range(1, 13)
]

for path in paths:
    path.mkdir(parents=True, exist_ok=True)

t = 3

targets = [
    str(Path.cwd()
    / f'reports/2020/Q{i // t}/{str(i - t + 1).zfill(2)}_sales')
    for i in range(t, t + 12)
]


parts = []
for target in targets:
    parts.append(target.split("\\")[:-1])
    
output = sorted(list(set(["/".join(part) for part in parts])))

for path in output:
    print(path)