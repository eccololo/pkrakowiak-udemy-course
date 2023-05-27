import os


fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]

paths = []
for name in fnames:
    full_path = os.path.join(os.getcwd(), name)
    paths.append(full_path)

print(paths)