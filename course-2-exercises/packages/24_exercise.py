import os

fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]
paths = []
base_dir = "eval"

for idx, fname in enumerate(fnames):
    if idx < 12:
        paths.append(os.path.join(base_dir, "2020", fname))
    else:
        paths.append(os.path.join(base_dir, "2021", fname))

for path in paths:
    print(path)
