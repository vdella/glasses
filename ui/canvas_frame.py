import tkinter as tk


class CanvasFrame:

    def __init__(self, mainframe: tk.Frame):
        self.canvas = tk.Canvas(mainframe, bg='white')
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
