import os


paths = [os.path.join(os.getcwd(), "Ex25", f'dir_{str(i).zfill(2)}') for i in range(1, 14)]
os.mkdir(os.path.join(os.getcwd(), "Ex25"))
for path in paths:
    if not os.path.exists(path):
        os.mkdir(path)

os.rmdir(paths[-1])
print(os.listdir(os.path.join(os.getcwd(), "Ex25")))