import tkinter as tk
from tkinter import ttk

# put const in settings file


# this handles the actual component making
class Component(ttk.Label):
    def __init__(
        self, master, text, in_buttons_count=1, out_buttons_count=1, func=None
    ):
        self.master = master
        self.make_component(text)  # this after making buttons?
        self.inputs = [0 for x in range(in_buttons_count)]
        self.outputs = [0 for x in range(out_buttons_count)]
        self.bind("<ButtonPress-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_drag_stop)
        self.make_buttons(in_buttons_count, out_buttons_count)
        self.func = func
        # button1 = ttk.Button(master=self, text="B")
        # button1.place(x=0, y=0, height=30, width=30)

    def handle_button_input(self, index):
        pass

    def make_buttons(self, in_buttons, out_buttons):
        # 30 is the button height
        height_coeff = 100 // (in_buttons + 1)  # 100px
        print(height_coeff)

        for i in range(1, in_buttons + 1):
            temp = ttk.Button(
                master=self,
                text="b",
                command=lambda: self.handle_button_input(i - 1),
            )
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

    def make_component(self, text):
        super().__init__(master=self.master, anchor="center", text=text)
        self.place(
            x=10,
            y=10,
            width=100,
            height=115,
        )


class IO(Component):
    def __init__(self, master, type, func, **kwargs):
        if type == "input":
            in_c = 0
            out_c = 1
        else:
            in_c = 1
            out_c = 0
        super().__init__(
            master=master,
            in_buttons_count=in_c,
            out_buttons_count=out_c,
            func=None,
            text=type,
        )


# this handles the component making
class MainCanvas(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        comp1 = Component(master=self, text="foobar")
        comp2 = Component(
            master=self, text="foobar", in_buttons_count=3, out_buttons_count=2
        )
        inp = IO(master=self, type="input", text="input", func=None)
        out = IO(master=self, type="output", text="input", func=None)


root = tk.Tk()
root.geometry("800x600")
root.title("what wha")

canvas = MainCanvas(root, background="grey", height=500, width=600)
canvas.pack()


root.mainloop()
