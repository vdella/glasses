from tkinter import *


class PointScanner:

    def __init__(self, mw):
        self.prompt = Toplevel(mw.root)
        self.prompt.title("Point prompt")
        self.prompt.geometry("200x200")

    def point_label_for(self, is_x_axis: bool):
        axis = 'X' if is_x_axis else 'Y'
        Label(self.prompt, text="Input {} for new point".format(axis)).pack()

    def parse(self) -> Entry:
        entry = Entry(self.prompt)
        entry.pack()
        return entry

    def enter_button(self):
        button_pressed = StringVar()
        enter = Button(self.prompt, text='Enter', command=lambda: button_pressed.set('button pressed'))
        enter.pack()
        enter.wait_variable(button_pressed)
        return enter

    def close(self):
        self.prompt.destroy()


class LineScanner(PointScanner):
    def __init__(self, mw):
        super().__init__(mw)
        self.prompt = Toplevel(mw.root)
        self.prompt.title("Line prompt")
        self.prompt.geometry("200x400")
