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

paths_dict = {}
file_names = [f"{str(i).zfill(2)}_music" for i in range(1, 6)]

for path in paths:
    files = [f"{file_name}.{random.choice(['mp3', 'wav'])}" for file_name in file_names]
    paths_dict[path] = files

pprint(paths_dict)
