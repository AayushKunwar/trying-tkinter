import tkinter as tk
from tkinter import ttk

# https://www.reddit.com/r/learnpython/comments/nary8j/tkinter_pass_reference_to_self_to_lambda_function/:w

# TODO: put const in settings file
# TODO FIXME XXX BUG HACK NOTE

# TODO: overlap the main frame with a canvas
# AND: use the update tension idea from 3rectangles.py file
# to handle the line update
# add update (lines) after drag_stop??


# this handles the actual component making
class Component(ttk.Label):
    button_selected = None

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

    def bind_card(self, card, another_card):
        x1, y1 = card.winfo_x(), card.winfo_y()
        print(x1, y1)

    def handle_button_input(self, button, type):
        print("button entered")
        print(button)
        if Component.button_selected == button:
            print("the same thing")
        if Component.button_selected == None:
            # pass
            if type == "input":
                Component.button_selected = button
                # print(Component.button_selected)
        else:
            if type == "output":
                self.bind_card(button, Component.button_selected)

        # elif type == "input":
        #     print("input")
        # else:
        #     print("output")

    def make_buttons(self, in_buttons, out_buttons):
        # 30 is the button height
        height_coeff = 100 // (in_buttons + 1)  # 100px
        print(height_coeff)

        for i in range(1, in_buttons + 1):
            index_counter = i - 1
            temp = ttk.Button(
                master=self,
                text=f"{index_counter}",
                # command=partial(self.handle_button_input, temp, "input"),
            )
            temp.place(x=0, y=i * height_coeff - (30 / 2), width=30, height=30)
            self.inputs.append(temp[i - 1])

        height_coeff = 100 // (out_buttons + 1)
        for i in range(1, out_buttons + 1):
            temp = ttk.Button(
                master=self,
                text="b",
                command=lambda: self.handle_button_input(button=self, type="output"),
            )
            temp.place(x=100 - 30, y=i * height_coeff - (30 / 2), width=30, height=30)
            self.outputs[i - 1] = temp

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


# this is the single input output
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
class App(tk.Canvas):
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

# canvas = tk.Canvas(master=root)
# canvas.place(x=100, y=50)


app = App(root, height=500, width=600, background="grey")
app.place(x=50, y=50)

foo = tk.Canvas.create_line(app, 1, 1, 100, 100, width=10)

root.mainloop()
