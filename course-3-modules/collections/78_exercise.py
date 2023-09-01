from collections import deque

wishlist = deque()
wishlist.append('003')
wishlist.append('001')
wishlist.append('004')
wishlist.append('002')
wishlist.append('005')
first_item = wishlist.popleft()
print(first_item)