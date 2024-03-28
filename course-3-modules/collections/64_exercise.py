from collections import namedtuple


Point = namedtuple(typename='Point', field_names=['x', 'y'])

pt1 = Point(3, 4)
pt2 = Point(-2, 6)

pt3 = Point((pt1.x + pt2.x) / 2, (pt1.y + pt2.y) / 2)

print(f"Point(x={pt3.x}, y={pt3.y})")