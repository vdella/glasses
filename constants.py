import pyautogui


class Window:
    X_MIN, Y_MIN = 0, 0
    X_MAX, Y_MAX = pyautogui.size()


class Canvas:
    X_MIN = 0
    X_MAX = Window.X_MAX / 2
    Y_MIN = 0
    Y_MAX = Window.Y_MAX / 2
