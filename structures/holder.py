class PointHolder:

    def __init__(self):
        self.points = set()

    def push(self, point):
        return self.points.add(point)

    def pop(self):
        return self.points.pop()
