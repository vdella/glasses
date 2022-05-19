from operations.paint import paint
from operations.viewport import viewport_transformation


def paint_graph(graph: dict, canvas):
    for key, value in graph.items():
        x1, y1 = viewport_transformation(key)
        x2, y2 = viewport_transformation(value)
        paint(x1, y1, x2, y2, canvas)


def draw_horizontal(canvas):
    x1, y1 = viewport_transformation((0, -3000))
    x2, y2 = viewport_transformation((0, 3000))
    canvas.create_line(x1, y1, x2, y2, fill='blue', width=5, dash=True)


def draw_vertical(canvas):
    x1, y1 = viewport_transformation((-3000, 0))
    x2, y2 = viewport_transformation((3000, 0))
    canvas.create_line(x1, y1, x2, y2, fill='orange', width=5, dash=True, dashoffset=5)
