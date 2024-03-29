from collections import Counter

fnames = [
    '001_image.png',
    '002_image.png',
    '003_image.jpg',
    '004_image.png',
    '005_image.png',
    '006_image.png',
    '007_image.jpg',
    '008_image.png',
    '009_image.jpg',
    '010_image.jpg',
    '011_image.jpg',
    '012_image.png',
    '013_image.jpg',
    '014_image.jpg',
    '015_image.jpg',
    '016_image.png',
    '017_image.jpg',
    '018_image.jpg',
    '019_image.png',
    '020_image.png',
    '021_image.jpg',
    '022_image.jpg',
    '023_image.png',
    '024_image.png',
    '025_image.jpg',
    '026_image.png',
    '027_image.png',
    '028_image.jpg',
    '029_image.png',
    '030_image.png',
]

output = Counter([name.split(".")[1] for name in fnames])
print(output)