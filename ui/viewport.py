def transform(point, window, viewport):
    # Keeps the X-axis...
    x_viewport = ((point.x - window.x.min) / (window.x.max - window.x.min)) * (viewport.x.max - viewport.x.min)

    # But inverts the Y's.
    y_viewport = (1 - (point.y - window.y.min) / (window.y.max - window.y.min)) * (viewport.y.max - viewport.y.min)

    return x_viewport, y_viewport
