import os
import random

random.seed(30)
images = [
    f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}"
    for i in range(1, 20)
]
images_jpg = []
images_png = []

base_dir = 'images'

if not os.path.exists(base_dir):
    os.mkdir(base_dir)
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')

if not os.path.exists(png_dir):
    os.mkdir(png_dir)
if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

# tutaj wpisz rozwiązanie
for image in images:
    if image.endswith(".jpg"):
        images_jpg.append(image)
    else:
        images_png.append(image)

for image in images_jpg:
    full_dir = os.path.join(jpg_dir, image)
    if not os.path.exists(full_dir):
        with open(full_dir, "w") as file:
            pass

for image in images_png:
    full_dir = os.path.join(png_dir, image)
    if not os.path.exists(full_dir):
        with open(full_dir, "w") as file:
            pass

for root, dirs, files in os.walk(base_dir):
    print(root)
    for file in sorted(files):
        print(f'\t{file}')
