from operations.paint import paint
from operations.geometry import viewport_transformation


def paint_graph(graph: dict, canvas):
    for key, value in graph.items():
        x1, y1 = viewport_transformation(key)
        x2, y2 = viewport_transformation(value)
        paint(x1, y1, x2, y2, canvas)
