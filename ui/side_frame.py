from tkinter import *


class SideFrame:

    def __init__(self, root, side, width, height):
        """Creates a frame for widget placement.
        The canvas is placed over a side frame, which is on the right side of the main window,
        while the other widgets are located on its left."""
        self.frame = Frame(root, width=width, height=height)
        self.frame.pack(side=side, fill=BOTH, expand=True)
