from constants import Window, Canvas


def viewport_transformation(point: tuple):
    # Keeps the X-axis...
    x, y = point

    x_viewport = ((x - Window.X_MIN) / (Window.X_MAX - Window.X_MIN)) * (Canvas.X_MAX - Canvas.X_MIN)

    # But inverts the Y's.
    y_viewport = (1 - (y - Window.Y_MIN) / (Window.Y_MAX - Window.Y_MIN)) * (Canvas.Y_MAX - Canvas.Y_MIN)

    return x_viewport, y_viewport
