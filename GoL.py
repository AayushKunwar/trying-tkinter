import tkinter as tk
from tkinter import ttk
import math
import time
import os

window = tk.Tk()
window.title("GoL")
window.geometry("700x700")

window_width = 600
box_count = 32
box_width = int(window_width / (box_count - 1))
# print(box_width)


def draw_box(x, y):
    global canvas
    # x,y is the box index
    x = x * box_width
    y = y * box_width
    canvas.create_rectangle((y, x, y + box_width, x + box_width), fill="red")


def modi(x, y):
    return (x % y + y) % y


def get_nbour(x, y):
    nbour_count = 0
    for xc in range(-1, 2):
        for xr in range(-1, 2):
            if xc == 0 and xr == 0:
                continue
            r = modi(x + xr, box_count)
            c = modi(y + xc, box_count)
            # if r >= 0 and r < box_count and c >= 0 and c < box_count:
            nbour_count += current_state[r][c]
    return nbour_count


def draw_current_state():
    global canvas
    canvas.delete("all")
    for r in range(box_count):
        for c in range(box_count):
            if current_state[r][c]:
                draw_box(x=r, y=c)


def next_step():
    global current_state
    global next_state
    for r in range(box_count):
        for c in range(box_count):
            nbour_alive = get_nbour(r, c)
            is_alive = current_state[r][c]
            if is_alive:
                if nbour_alive in range(2, 4):
                    next_state[r][c] = 1
                else:
                    next_state[r][c] = 0
            else:
                if nbour_alive == 3:
                    next_state[r][c] = 1
                else:
                    next_state[r][c] = 0
    current_state = next_state
    next_state = make_empty_state()
    draw_current_state()


def make_empty_state():
    return [[0 for _ in range(box_count)] for _ in range(box_count)]


def autoplay_handler():
    if is_play.get():
        next_step()
        window.after(300, autoplay_handler)


def toggle_autoplay():
    global is_play
    is_play.set(not is_play.get())
    auto_play_name.set(f"Autoplay: {is_play.get()}")
    autoplay_handler()


current_state = make_empty_state()
next_state = make_empty_state()

top_frame = ttk.Frame(window, height=100)
top_frame.pack()

next_button = ttk.Button(top_frame, text="Next", command=next_step)
next_button.pack(side="left")

is_play = tk.BooleanVar(value=False)
auto_play_name = tk.StringVar(value=f"Autoplay: {is_play.get()}")
auto_play = ttk.Button(
    top_frame,
    text="Autoplay: False",
    command=toggle_autoplay,
    textvariable=auto_play_name,
)
auto_play.pack(side="left")

canvas = tk.Canvas(
    window, bg="#181818", width=window_width + 4, height=window_width + 4
)
canvas.pack()


def callback(event):
    # scaling broken
    # scale = box_count / (window_width - 10)
    c = math.floor(event.x / box_width)
    r = math.floor(event.y / box_width)
    # print(event.x, event.y, "and", r, c)
    current_state[r][c] = (current_state[r][c] + 1) % 2
    draw_current_state()


canvas.bind("<Button-1>", callback)

# draw_box(can=canvas, x=100, y=100)
current_state[0][3] = 1
draw_current_state()

window.mainloop()

# TODO: implement mouse drag drawing
# TODO: implement other cellular automatons?? brians brain??
