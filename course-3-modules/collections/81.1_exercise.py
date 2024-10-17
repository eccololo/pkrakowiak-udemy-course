from collections import deque


user_ids = ['003', '001', '004', '006', '002', '005']

wishlist = deque(maxlen=3)

for uid in user_ids:
    wishlist.append(uid)
    print(wishlist)