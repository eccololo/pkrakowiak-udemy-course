import os


base_dir = 'images'
base_dir_path = os.path.join(os.getcwd(), base_dir)
if not os.path.exists(base_dir_path):
    os.mkdir(base_dir_path)
os.chdir(base_dir_path)
images_png_path = os.path.join(base_dir_path, "images_png")
if not os.path.exists(images_png_path):
    os.mkdir(os.path.join(base_dir_path, "images_png"))

for root, dirs, files in os.walk(base_dir):
    print(root)