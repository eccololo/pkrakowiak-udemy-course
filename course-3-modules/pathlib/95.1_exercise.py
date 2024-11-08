from pathlib import Path


paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}' for i in range(1, 13)]

for path in paths:
    path.mkdir(parents=True, exist_ok=True)

for path in paths:
    new_path = path.parent / (f"{path.name}_sales")
    
    if not new_path.exists():
        path.rename(new_path)
    else:
        print("This path already exists!")

# directory = Path('/eval/reports/2020/')

directory = Path(Path.cwd() /  'reports/2020/')

directories = sorted([d.name for d in directory.iterdir() if d.is_dir()])

for d in directories:
    print(d)