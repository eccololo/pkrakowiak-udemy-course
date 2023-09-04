from pathlib import Path

paths = []
path_part = "eval/reports/2020/__"

for i in range(1, 13):
    if i < 10:
        paths.append(Path.cwd() / Path(path_part.replace("__", f"0{i}")))
    else:
        paths.append(Path.cwd() / Path(path_part.replace("__", f"{i}")))

for path in paths:
    print(path)
    if not Path.is_dir(path):
        Path.mkdir(path, parents=True)

# Other solution
# paths = [
#     Path.cwd() / f'reports/2020/{str(i).zfill(2)}'
#     for i in range(1, 13)
# ]
#
# for path in paths:
#     path.mkdir(parents=True)