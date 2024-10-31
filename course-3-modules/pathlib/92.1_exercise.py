from pathlib import Path, PosixPath

list_of_paths = [Path.cwd() / f'eval/reports/2020/{str(i).zfill(2)}' for i in range(1, 13)]

for part in list_of_paths:
    if not part.is_dir():
        part.mkdir(parents=True)

for part in sorted(list_of_paths):
    print(part)