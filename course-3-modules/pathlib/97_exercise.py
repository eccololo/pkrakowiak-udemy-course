from pathlib import Path

paths = [
    Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales'
    for i in range(1, 13)
]

for path in paths:
    path.mkdir(parents=True)

t = 3
targets = [
    Path.cwd()
    / f'reports/2020/Q{i // t}/{str(i - t + 1).zfill(2)}_sales'
    for i in range(t, t + 12)
]

for target in targets:
    if not target.parent.is_dir():
        target.mkdir(parents=True)

for path, target in zip(paths, targets):
    path.rename(target)

for dir in sorted(Path.cwd().joinpath('reports/2020').iterdir()):
    print(dir)