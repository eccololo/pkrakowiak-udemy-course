# [IN]: r1 = Rectangle(4, 5)
# [IN]: r2 = Rectangle(4, 5)
# [IN]: r3 = Rectangle(2, 3)
#
# [IN]: r1 == r2
# [OUT]: True
#
# [IN]: r1 == r3
# [IN]: False


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __eq__(self, target):
        return target.width == self.width and target.height == self.height

