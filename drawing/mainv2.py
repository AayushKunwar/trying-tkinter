import tkinter as tk
from tkinter import ttk

# put const in settings file


class Component(ttk.Label):
    def __init__(
        self, master, in_buttons_count=1, out_buttons_count=1, func=None, **kwargs
    ):
        self.master = master
        self.make_component(**kwargs)  # this after making buttons?
        self.bind("<ButtonPress-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_drag_stop)
        self.make_buttons(in_buttons_count, out_buttons_count)
        self.put_func(func)
        # button1 = ttk.Button(master=self, text="B")
        # button1.place(x=0, y=0, height=30, width=30)

    def put_func(self, func):
        self.func = func

    def make_buttons(self, in_buttons, out_buttons):
        # 30 is the button height
        height_coeff = 100 // (in_buttons + 1)  # 100px
        print(height_coeff)
        for i in range(1, in_buttons + 1):
            temp = ttk.Button(master=self, text="b")
            temp.place(x=0, y=i * height_coeff - (30 / 2), width=30, height=30)
        height_coeff = 100 // (out_buttons + 1)
        for i in range(1, out_buttons + 1):
            temp = ttk.Button(master=self, text="b")
            temp.place(x=100 - 30, y=i * height_coeff - (30 / 2), width=30, height=30)

    def on_drag_start(self, event):
        # self.active = self
        self.drag_data = {"x": event.x, "y": event.y}

    def on_drag(self, event):
        newx = self.winfo_x() - self.drag_data["x"] + event.x
        newy = self.winfo_y() - self.drag_data["y"] + event.y
        self.place(x=newx, y=newy)

    def on_drag_stop(self, event):
        # self.active = None
        pass

    def make_component(self, **kwargs):
        super().__init__(master=self.master, anchor="center", **kwargs)
        self.place(
            x=10,
            y=10,
            width=100,
            height=115,
        )


class MainCanvas(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        comp1 = Component(master=self, text="foobar")
        comp2 = Component(
            master=self, text="foobar", in_buttons_count=3, out_buttons_count=2
        )


root = tk.Tk()
root.geometry("800x600")
root.title("what wha")

canvas = MainCanvas(root, background="grey", height=500, width=600)
canvas.pack()


root.mainloop()
