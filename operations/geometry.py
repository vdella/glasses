from constants import Window, Viewport


def viewport_transformation(point: tuple):
    # Keeps the X-axis...
    x, y = point[0], point[1]

    x_viewport = ((x - Window.X_MIN) / (Window.X_MAX - Window.X_MIN)) * (Viewport.X_MAX - Viewport.X_MIN)

    # But inverts the Y's.
    y_viewport = (1 - (y - Window.Y_MIN) / (Window.Y_MAX - Window.Y_MIN)) * (Viewport.Y_MAX - Viewport.Y_MIN)

    return x_viewport, y_viewport
