import os

fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]

output_paths = []
for item in fnames:
    output_paths.append(os.path.join(os.getcwd(), item))

print(output_paths)