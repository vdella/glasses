class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


class Line:

    def __init__(self, src_point, dst_point):
        self.pointA = src_point
        self.pointB = dst_point

    def __str__(self):
        print('src = ({}, {}), dst = ({}, {})'.format(
            self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y
        ))
