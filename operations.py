from structures.simple import Point


class Constants:
    class Window:  # As the root's dimensions.
        X_MIN = 0
        X_MAX = 750

        Y_MIN = 0
        Y_MAX = 500

    class Viewport:  # As the root's Canvas dimensions.
        X_MIN = 0
        X_MAX = 750 / 2

        Y_MIN = 0
        Y_MAX = 500 / 2


def viewport_transformation(point):
    # Keeps the X-axis...
    x_viewport = ((point.x - Constants.Window.X_MIN) / (Constants.Window.X_MAX - Constants.Window.X_MIN)) \
        * (Constants.Viewport.X_MAX - Constants.Viewport.X_MIN)

    # But inverts the Y's.
    y_viewport = (1 - (point.y - Constants.Window.Y_MIN) / (Constants.Window.Y_MAX - Constants.Window.Y_MIN)) \
        * (Constants.Viewport.Y_MAX - Constants.Viewport.Y_MIN)

    return Point(x_viewport, y_viewport)
