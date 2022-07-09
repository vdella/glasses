from constants import *


def viewport_transformation(point: tuple):
    # Keeps the X-axis...
    x, y = point

    x_viewport = ((x - X_MIN) / (X_MAX - X_MIN)) * (X_MAX - X_MIN)

    # But inverts the Y's.
    y_viewport = (1 - (y - Y_MIN) / (Y_MAX - Y_MIN)) * (Y_MAX - Y_MIN)

    return x_viewport, y_viewport
