from tkinter import Canvas


def paint(x1, y1, x2, y2, canvas: Canvas) -> ():
    """Paints the outlined extremes of a line and the line itself."""
    canvas.create_oval(x1, y1, x1, y1, fill='white', outline='white', width=5)
    canvas.create_oval(x2, y2, x2, y2, fill='white', outline='white', width=5)
    canvas.create_line(x1, y1, x2, y2, fill='white')
