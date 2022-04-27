from tkinter import *
from structures.holder import PointHolder
from structures.simple import Point


class MainWindow:

    __WIDTH, __HEIGHT = 750, 500
    __BASIC_COLOR = 'black'
    __DOT_SIZE = 3

    def __init__(self):
        self.points = PointHolder()

        self.root = self.root()

        self.canvas = self.canvas()

        self.general_menu = self.general_menu()

        self.creation_menu = self.creation_menu()

        self.panel = self.panel()

        self.root.mainloop()

    def root(self):
        root = Tk()
        root.title('Glasses')
        root.geometry("{}x{}".format(self.__WIDTH, self.__HEIGHT))
        return root

    def paint(self, point):
        # get x1, y1, x2, y2 coordinates
        x1, y1 = (point.x - self.__DOT_SIZE), (point.y - self.__DOT_SIZE)
        x2, y2 = (point.x + self.__DOT_SIZE), (point.y + self.__DOT_SIZE)

        self.canvas.create_oval(x1, y1, x2, y2, fill=self.__BASIC_COLOR, outline=self.__BASIC_COLOR)
        self.points.push(Point(point.x, point.y))

    def canvas(self):
        canvas = Canvas(self.root, width=self.__WIDTH / 2, height=self.__HEIGHT / 2, bg='white')
        canvas.bind('<Button-1>', func=self.paint)
        canvas.pack()
        return canvas

    def general_menu(self):
        general_menu = Menu(self.root)
        self.root.config(menu=general_menu)
        return general_menu

    def creation_menu(self):
        creation_menu = Menu(self.general_menu, tearoff=False)
        self.general_menu.add_cascade(label='Create', menu=creation_menu)

        creation_menu.add_command(label='Point', command=self.read_point_input)
        creation_menu.add_command(label='Line')

        return creation_menu

    def panel(self):
        panel = PanedWindow(self.root, orient=HORIZONTAL)
        Label(panel, text='Created objects').pack(side=LEFT)
        panel.pack(fill=BOTH)
        return panel

    def read_point_input(self):
        prompt = Toplevel(self.root)
        prompt.title("Point prompt")
        prompt.geometry("200x200")

        Label(prompt, text="Input X for new point").pack()

        input_x = Entry(prompt)
        input_x.pack()

        Label(prompt, text="Input Y for new point").pack()

        input_y = Entry(prompt)
        input_y.pack()

        button_pressed = StringVar()

        enter = Button(prompt, text='Enter', command=lambda: button_pressed.set('button pressed'))
        enter.pack()
        enter.wait_variable(button_pressed)

        x = input_x.get()
        y = input_y.get()

        return int(x), int(y)
