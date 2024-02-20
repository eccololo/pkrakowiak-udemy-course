import os
import random

random.seed(30)
images = [
    f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}"
    for i in range(1, 20)
]

base_dir = 'images'

if not os.path.exists(base_dir):
    os.mkdir(base_dir)
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')

if not os.path.exists(png_dir):
    os.mkdir(png_dir)
if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

# Tutaj wpisz swoje rozwiązanie

path = os.getcwd()
path_to_png = os.path.join(path, png_dir)
path_to_jpg = os.path.join(path, jpg_dir)
for image in images:
    if image.endswith("png"):
        if not os.path.exists(os.path.join(path_to_png, image)):
            file = open(os.path.join(path_to_png, image), "a")
            file.close()
    else:
        if not os.path.exists(os.path.join(path_to_jpg, image)):
            file = open(os.path.join(path_to_jpg, image), "a")
            file.close()


for root, dirs, files in os.walk(base_dir):
    print(root)
    for file in sorted(files):
        print(f'\t{file}')