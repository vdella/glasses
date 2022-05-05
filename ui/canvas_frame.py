import tkinter as tk


class CanvasFrame:

    def __init__(self, mainframe: tk.Frame, width, height):
        self.canvas = tk.Canvas(mainframe, width=0.60*width, height=height, bg='white')
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
