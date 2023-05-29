import tkinter as tk


class Button:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.draw_button()

    def draw_button(self):
        self.canvas.create_rectangle(self.x, self.y, 30, 30, fill="blue")

    def update_coords(self, posx, posy):
        pass


class Component:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.item = None
        self.tag = "component"
        # self.draw_card()
        self.buttons = []
        self.draw_card()

    # this for initialization only
    def draw_card(self, color="red"):
        reference = self.canvas.create_rectangle(
            self.x, self.y, self.width + self.x, self.height + self.y, fill=color
        )
        foo = Button(self.canvas, 10, 10)
        # self.add_button(foo)
        self.item = reference

    def update_coords(self, x, y):
        width = self.width
        height = self.height
        # position = coords[0], coords[1]

        x1 = x - width / 2
        y1 = y - height / 2
        x2 = x + width / 2
        y2 = y + height / 2

        self.canvas.coords(self.item, x1, y1, x2, y2)

    def on_click(self, event):
        print("clicked this ")

    def add_button(self, btn):
        self.buttons.append(btn)


# component maker, canvas handler
class Main_Can(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.active = None

        card1 = Component(canvas=self, x=10, y=10)
        card2 = Component(canvas=self, x=100, y=200)
        # button = tk.Button(card1, text="what what")
        # button.place(x=2, y=2)
        self.components = {}
        self.components.update({card1.item: card1})
        self.components.update({card2.item: card2})

        # this to be called only once?
        # self.draw_components()

        self.bind("<ButtonPress-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_drag_stop)

    def draw_components(self):
        # print(self.components)
        for component in self.components.values():
            component.draw_card()

    def on_drag_stop(self, event):
        self.active = None

    def on_drag_start(self, event):
        # can be component OR BUTTONS
        item = self.find_closest(event.x, event.y)
        print(item)
        try:
            # item = self.find_withtag("current")
            x1, y1, x2, y2 = self.coords(item[0])
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.active = item[0]
        except IndexError:
            print("no item was clicked")

    def on_drag(self, event):
        if self.active == None:
            return
        coords = self.coords(self.active)
        width = coords[2] - coords[0]
        height = coords[1] - coords[3]
        position = coords[0], coords[1]

        x1 = event.x - width / 2
        y1 = event.y - height / 2
        x2 = event.x + width / 2
        y2 = event.y + height / 2
        # x=self.winfo_x() + (event.x - self.drag_data["x"]),

        try:
            self.components[self.active].update_coords(event.x, event.y)
        except KeyError:
            # print(self.active)
            pass
        # self.coords(self.active, x1, y1, x2, y2)


root = tk.Tk()
# root.state("zoomed")
root.geometry("600x600")

main_canvas = Main_Can(master=root, bg="skyblue")
main_canvas.pack(fill="both", expand=1)

root.mainloop()
