from view.canvas_frame import CanvasFrame
from view.root_window import root
from view.paint_interface import draw_horizontal, draw_vertical, draw_origin
from view.menu import FileMenu


class Application:

    width, height = root.winfo_screenwidth(), root.winfo_screenheight()

    def __init__(self):
        self.root = root

        self.canvas_frame = CanvasFrame(self.root)

        self.file_menu = FileMenu(self.root, self.canvas_frame.canvas)

        draw_horizontal(self.canvas_frame.canvas)
        draw_vertical(self.canvas_frame.canvas)
        draw_origin(self.canvas_frame.canvas)

        self.root.mainloop()


if __name__ == '__main__':
    Application()
