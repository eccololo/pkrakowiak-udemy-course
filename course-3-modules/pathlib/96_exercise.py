from pathlib import Path


paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'
    for i in range(1, 13)
]

paths_updated = []

path_parent = paths[0].parent
quartal = None
for i, path in enumerate(paths, start=1):
    if i <= 3:
        quartal = "Q1"
    elif i <= 6:
        quartal = "Q2"
    elif i <= 9:
        quartal = "Q3"
    else:
        quartal = "Q4"

    parent = path.parent
    file_name = path.name
    print(f"{parent}\\{quartal}\\{file_name}")

