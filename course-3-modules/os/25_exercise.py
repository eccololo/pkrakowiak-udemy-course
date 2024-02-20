import os


paths = [os.path.join(os.getcwd(), f'dir_{str(i).zfill(2)}') for i in range(1, 14)]

for item in paths:
    if not os.path.exists(item):
        os.mkdir(item)

os.rmdir(os.path.join(os.getcwd(), "dir_13"))

output = []
for item in os.listdir(os.getcwd()):
    if len(item) == 6:
        output.append(item)

print(sorted(output))