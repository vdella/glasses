from constants import Window


center = Window.X_MAX / 2, Window.Y_MAX / 2


def up():
    x, y = center
    x += 10
    return x, y


def down():
    x, y = center
    x -= 10
    return x, y


def left():
    x, y = center
    y -= 10
    return x, y


def right():
    x, y = center
    y += 10
    return x, y
