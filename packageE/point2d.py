class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __repr__(self):
        return "Point2D(x={},y=a{})".format(self.x, self.y)

if __name__ == '__main__':
    pointA = Point2D(2,2)
    pointB = Point2D(3,4)

    print(str(pointA))
    print(repr(pointA))