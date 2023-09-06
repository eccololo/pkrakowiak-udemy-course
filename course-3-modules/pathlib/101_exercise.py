from pathlib import Path
from pprint import pprint
import random


random.seed(42)
paths = [
    Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}'
    for i in range(1, 7)
]

for path in paths:
    if not Path.is_dir(path):
        path.mkdir(parents=True)

paths_dict = {
    path: [
        f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}"
        for i in range(1, 6)
    ]
    for path in paths
}

fname_paths = []
for path, fnames in paths_dict.items():
    for fname in fnames:
        fname_paths.append(path.joinpath(fname))

mp3s = []
for path in fname_paths:
    if not Path.is_file(path):
        with open(path, "w") as f:
            pass
    if str(path).endswith("mp3"):
        mp3s.append(path)

for mp3_path in sorted(mp3s):
    print(mp3_path)
