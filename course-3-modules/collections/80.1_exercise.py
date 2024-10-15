from collections import deque


user_ids = ['003', '001', '004', None, '002', '005']

wishlist =  deque()

for uid in user_ids:
    if uid is None:
        wishlist.clear()
    else:
        wishlist.append(uid)

print(wishlist)