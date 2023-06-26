path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

is_youtube = path1.find("youtube")
if is_youtube != -1:
    is_youtube = True
else:
    is_youtube = False

print(f"path1: {is_youtube}")

is_youtube = path2.find("youtube")
if is_youtube != -1:
    is_youtube = True
else:
    is_youtube = False
print(f"path2: {is_youtube}")