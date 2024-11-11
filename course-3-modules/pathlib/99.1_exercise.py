from pathlib import Path
from pprint import pprint


paths = [Path.cwd() / f"media/music/playlist_{str(i).zfill(2)}" for i in range(1, 11)]

for path in paths:
    if not path.exists():
        path.mkdir(exist_ok=True, parents=True)
    
    print(path)