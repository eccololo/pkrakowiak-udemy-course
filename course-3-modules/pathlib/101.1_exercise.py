from pathlib import Path
from pprint import pprint
import random


random.seed(42)
paths = [
    Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}'
    for i in range(1, 7)
]

for path in paths:
    if not path.exists():
        path.mkdir(parents=True)


paths_dict = {
    path: [
        f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}"
        for i in range(1, 6)
    ]
    for path in paths
}

fname_paths = []
for key, value in paths_dict.items():
    for file in value:
        fullpath = key.joinpath(file)
        fname_paths.append(fullpath)


for path in fname_paths:
    pprint(path)
