import numpy as np
from math import sin, cos


def scale_factor(point2d: tuple):
    """Adapts a 2D point for a 3D environment in order
    to multiply 3x3 matrices for translation, rotation and
    scaling."""
    return point2d[0], point2d[1], 1


def translate(point2d: tuple, distance: tuple):
    scaled_point = scale_factor(point2d)
    dx, dy = distance
    return dot(scaled_point, [[1, 0, 0],
                              [0, 1, 0],
                              [dx, dy, 1]])


def scale(point2d: tuple, delta: tuple):
    scaled_point = scale_factor(point2d)
    sx, sy = delta
    return dot(scaled_point, [[sx, 0, 0],
                              [0, sy, 0],
                              [0, 0, 1]])


def rotate(point2d, angle):
    scaled_point = scale_factor(point2d)
    return dot(scaled_point, [[cos(angle), - sin(angle), 0],
                              [sin(angle), cos(angle), 0],
                              [0, 0, 1]])


def dot(line_matrix, squared_matrix):
    return np.dot(line_matrix, squared_matrix).tolist()


if __name__ == '__main__':
    # print(scale_factor((0, 0)))
    line = [20, 33, 1]
    square = [[1, 0, 0],
              [0, 1, 0],
              [3, 5, 1]]
    # print(dot(line, square))
    print(translate((7, 5), (3, -4)))
