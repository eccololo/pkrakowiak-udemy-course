from collections import deque

user_ids = ['003', '001', '004', '002', '005']

wishlist = deque(user_ids)
wishlist.extend(['007', '009', '010'])

print(wishlist)
