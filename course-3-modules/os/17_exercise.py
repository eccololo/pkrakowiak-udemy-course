import os

names = [item for item in os.listdir(os.getcwd()) if item.endswith("py")]

print(sorted(names))