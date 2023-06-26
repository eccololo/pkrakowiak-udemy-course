from importlib.resources import path
import os
# print(dir(os))

# Printuje current working directory
# print(os.getcwd())

# Zmienia current working directory
# os.chdir("..")
# print(os.getcwd())

# Mozemy wykonywac polecenia UNIXowe
# os.system("mkdir dir1 dir2")

# Usuwanie katalogu.
# os.rmdir("dir1")

# Zwraca listę wszystkich plikow i katalogow w katalogu roboczym
# print(os.listdir())

# for item in os.listdir():
#     print(item)

# for item in os.listdir():
#     if item.endswith(".py"):
#         print(item)

# Wyprintowanie katalogu glownego, wszystkich katalogow i plikow w katalogu roboczym
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)

path_files = os.path.join(r"home\bath\dir", "script.py")
print(path_files)
