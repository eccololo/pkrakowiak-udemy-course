import os

images_path = os.path.join(os.getcwd(), 'images')
os.mkdir(images_path)
os.chdir(images_path)
print(os.getcwd())