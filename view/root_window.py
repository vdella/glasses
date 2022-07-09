from tkinter import *
from constants import X_MAX, Y_MAX


def create_root():
    root_window = Tk()
    root_window.title('Glasses')

    width, height = X_MAX, Y_MAX

    root_window.minsize(width, height)
    root_window.maxsize(width, height)

    return root_window


root = create_root()
