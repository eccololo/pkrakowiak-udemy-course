from pathlib import Path

paths = [Path.cwd() / f"eval/media/music/playlist_{str(i).zfill(2)}" for i in range(1, 11)]

for path in paths:
    if not Path.is_dir(path):
        Path.mkdir(path, parents=True)

for path in paths:
    print(path)