from pathlib import Path
from pprint import pprint

paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}' for i in range(1, 13)]
paths_renamed = []

for path in paths:
    if not Path.is_dir(path):
        path.mkdir(parents=True)

for i, path in enumerate(paths, start=1):
    paths_renamed.append(Path.rename(path, Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'))

pprint(paths_renamed)