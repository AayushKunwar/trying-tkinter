import tkinter as tk
from cell import Cell
import settings
import utils

root = tk.Tk()
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)

top_frame = tk.Frame(
    master=root, background="grey", width=1440, height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = tk.Frame(
    master=root,
    background="blue",
    width=utils.width_prct(25),
    height=utils.height_prct(75),
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = tk.Frame(
    master=root,
    background="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75),
)

center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_obj.grid(column=x, row=y)

Cell.randomize_mines()

root.mainloop()
