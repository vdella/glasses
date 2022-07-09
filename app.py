from view.canvas_frame import CanvasFrame
from view.root_window import root
from view.paint_interface import draw_horizontal, draw_vertical, draw_origin
from view.menu import FileMenu
from view.prompt import Prompt
from view.created_objects_frame import CreatedObjectsFrame
from tkinter import Tk


class Application:

    width, height = root.winfo_screenwidth(), root.winfo_screenheight()

    def __init__(self):
        self.root: Tk = root

        self.canvas_frame = CanvasFrame(self.root)
        self.created_objects_frame = CreatedObjectsFrame(self.root)
        self.prompt_frame = Prompt(self.root, self.canvas_frame, self.created_objects_frame)
        menu_frames = (self.prompt_frame, self.canvas_frame, self.created_objects_frame)

        self.file_menu = FileMenu(self.root, menu_frames)

        draw_horizontal(self.canvas_frame.canvas)
        draw_vertical(self.canvas_frame.canvas)
        draw_origin(self.canvas_frame.canvas)

        self.root.mainloop()


if __name__ == '__main__':
    Application()
