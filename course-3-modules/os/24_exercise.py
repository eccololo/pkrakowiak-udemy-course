import os

fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]

output_paths = []
for i, item in enumerate(fnames):
    if i < 13:
        output_paths.append(os.path.join(os.getcwd(), '2020', item))
    else:
        output_paths.append(os.path.join(os.getcwd(), '2021', item))

for item in output_paths:
    print(item)