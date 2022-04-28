class Dot:
    COLOR = 'black'
    SIZE = 3


class Window:  # As the root's dimensions.
    X_MIN = 0
    X_MAX = 750

    Y_MIN = 0
    Y_MAX = 500


class Viewport:  # As the root's Canvas dimensions.
    X_MIN = 0
    X_MAX = Window.X_MAX / 2

    Y_MIN = 0
    Y_MAX = Window.Y_MAX / 2
