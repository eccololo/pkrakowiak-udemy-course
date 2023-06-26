# [IN]: r1 = Rectangle(4, 5)
# [IN]: r2 = Rectangle(2, 3)
# [IN]: r3 = Rectangle(8, 2)
#
# [IN]: r1 + r2
# [OUT]: Rectangle(6, 8)
#
# [IN]: r1 + r3
# [IN]: Rectangle(12, 7)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    # Enter your solution here

    def __add__(self, target):
        return f'Rectangle({self.width + target.width}, {self.height + target.height})'


r1 = Rectangle(4, 5)
r2 = Rectangle(2, 3)
print(r1 + r2)
# [OUT]: Rectangle(6, 8)
