class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __repr__(self):
        return "Point2D(x={},y=a{})".format(self.x, self.y)

    def __format__(self, f):
        if f == 'r':
            return "[{},{}]".format(self.y, self.x)
        else:
            return "[{},{}]".format(self.x, self.y)

if __name__ == '__main__':
    pointA = Point2D(2,2)
    pointB = Point2D(3,4)

    print(str(pointA))
    print(repr(pointA))
    print("The point is {}".format(pointB))
    print("The point is {!r}".format(pointA))
    print("The point is {!s}".format(pointA))

    all_points_to_100 = [Point2D(x, y) for x in range(10) for y in range(10)]

    import reprlib

    print(reprlib.repr(all_points_to_100))