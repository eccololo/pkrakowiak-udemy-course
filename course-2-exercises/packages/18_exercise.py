import os

# print(help(os.mkdir))

new_dir = os.path.join(os.getcwd(), "images")
os.mkdir(new_dir)
os.chdir(new_dir)
print(os.getcwd())