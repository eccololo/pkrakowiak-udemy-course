from collections import deque

user_ids = ['003', '001', '004', None, '002', '005']

wishlist = deque()
for idx, item in enumerate(user_ids):
    if item is None:
        wishlist.extend(user_ids[idx+1:])
        break

print(wishlist)