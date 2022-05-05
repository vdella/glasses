import pyautogui


class Window:
    X_MIN, Y_MIN = 0, 0
    X_MAX, Y_MAX = pyautogui.size()


class Viewport:
    X_MIN = 0
    X_MAX = Window.X_MAX
    Y_MIN = 0
    Y_MAX = Window.Y_MAX / 2
