from pathlib import Path


paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'
    for i in range(1, 13)
]

for path in paths:
    if not Path.is_dir(path):
        Path.mkdir(path, parents=True)

for path in Path.iterdir(paths[0].parent):
    if path.is_dir():
        print(path)