import math

fnames = {
    '01_stream.txt',
    '02_stream.txt',
    '03_stream.txt',
    '04_stream.txt',
    '05_stream.txt',
}

perms = math.perm(len(fnames), len(fnames))
print(perms)
