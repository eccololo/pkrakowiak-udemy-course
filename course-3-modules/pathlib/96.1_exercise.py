from pathlib import Path


paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'
    for i in range(1, 13)
]


for path in paths:
    if not path.exists():
        path.mkdir(parents=True)

directories = sorted([dir for dir in paths])

for path in directories:
    print(path)