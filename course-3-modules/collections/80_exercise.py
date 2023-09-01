from collections import deque


user_ids = ['003', '001', '004', '006', '002', '005']

wishlist = deque(maxlen=3)

for item in user_ids:
    wishlist.append(item)
    if len(wishlist) >= 4:
        wishlist.rotate(-1)
        wishlist.pop()
    print(wishlist)


# Other solution
# wishlist = deque(maxlen=3)
# for user_id in user_ids:
#     wishlist.append(user_id)
#     print(wishlist)
