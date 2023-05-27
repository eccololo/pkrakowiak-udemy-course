import os

names = sorted([name for name in os.listdir() if name.endswith(".py")])

print(names)