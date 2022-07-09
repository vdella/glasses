from constants import X_MAX, Y_MAX
from view.paint import paint
from model.window.viewport import viewport_transformation


def paint_graph(graph: dict, canvas):
    for key, value in graph.items():
        x1, y1 = viewport_transformation(key)
        x2, y2 = viewport_transformation(value)
        paint(x1, y1, x2, y2, canvas)


def draw_vertical(canvas):
    x1, y1 = viewport_transformation((350, -3000))
    x2, y2 = viewport_transformation((350, 3000))
    canvas.create_line(x1, y1, x2, y2, fill='white', width=2, dash=True)


def draw_horizontal(canvas):
    x1, y1 = viewport_transformation((-3000, 350))
    x2, y2 = viewport_transformation((3000, 350))
    canvas.create_line(x1, y1, x2, y2, fill='white', width=2, dash=True, dashoffset=5)


def draw_origin(canvas):
    x1, y1 = viewport_transformation((X_MAX / 2, Y_MAX / 2))
    canvas.create_oval(x1 + 3, y1 + 3, x1 - 3, y1 - 3, fill="white")
