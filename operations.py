from structures.simple import Point
from constants import Window, Viewport


def viewport_transformation(point):
    # Keeps the X-axis...
    x_viewport = ((point.x - Window.X_MIN) / (Window.X_MAX - Window.X_MIN)) * (Viewport.X_MAX - Viewport.X_MIN)

    # But inverts the Y's.
    y_viewport = (1 - (point.y - Window.Y_MIN) / (Window.Y_MAX - Window.Y_MIN)) * (Viewport.Y_MAX - Viewport.Y_MIN)

    return Point(x_viewport, y_viewport)
