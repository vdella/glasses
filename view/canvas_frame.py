import tkinter as tk


class CanvasFrame:

    def __init__(self, root):
        self.canvas = tk.Canvas(root, bg='black')
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
