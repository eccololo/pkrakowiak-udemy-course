import os

names = [name for name in os.listdir() if name.startswith("e")]
names.sort()

print(names)