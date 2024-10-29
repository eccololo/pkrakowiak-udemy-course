from pathlib import Path

cwd = Path.cwd()
to_create = cwd / "reports"

if not to_create.is_dir():
    to_create.mkdir(exist_ok=True)

directories = sorted([p for p in cwd.iterdir() if p.is_dir()])

for directory in directories:
    print(directory)