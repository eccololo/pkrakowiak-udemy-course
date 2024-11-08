from pathlib import Path


paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'
    for i in range(1, 13)
]

for path in paths:
    idx = path.parts.index("2020") + 1
    file = path.name
    month = file.split("_")[0]
    path_part = Path(*path.parts[:idx])
    if 3 >= int(month) >= 1:
        path_part = path_part.joinpath(f"Q1\{path.name}")
    if 6 >= int(month) >= 4:
        path_part = path_part.joinpath(f"Q2\{path.name}")
    if 9 >= int(month) >= 7:
        path_part = path_part.joinpath(f"Q3\{path.name}")
    if 12 >= int(month) >= 10:
        path_part = path_part.joinpath(f"Q4\{path.name}")

    print(path_part)