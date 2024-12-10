from pathlib import Path
from pprint import pprint
import random

paths_dict = {}

random.seed(42)
paths = [
    Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}'
    for i in range(1, 7)
]

for path in paths:
    if not path.exists():
        path.mkdir(parents=True)

for path in paths:
    paths_dict[path] = []
    for i in range(1, 6):
        paths_dict[path].append(str(i).zfill(1) + f"_music.{random.choice(["wav", "mp3"])}")


pprint(paths_dict)