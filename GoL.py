import tkinter as tk
from tkinter import ttk
import math

window = tk.Tk()
window.title("GoL")
window.geometry("600x600")

window_width = 600
box_count = 5
box_width = int(window_width / box_count)
print(box_width)


def draw_box(x, y):
    global canvas
    # x,y is the box index
    x = x * box_width
    y = y * box_width
    print(f"x:{x} and y:{y}")
    canvas.create_rectangle((y, x, y + box_width, x + box_width), fill="red")


def get_nbour(x, y):
    nbour_count = 0
    for xc in range(-1, 1):
        for xr in range(-1, 1):
            if xc == 0 and xr == 0:
                break
            r = x + xr
            c = y + xc
            if r >= 0 and r <= box_count and y >= 0 and y <= box_count:
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
    print("next step")
    global current_state
    global next_state
    for r in range(box_count):
        for c in range(box_count):
            nbour_alive = get_nbour(r, c)
            print(nbour_alive)
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
    print("next")
    print(next_state)
    print(current_state)
    draw_current_state()


current_state = [[0 for _ in range(box_count)] for _ in range(box_count)]
next_state = [[0 for _ in range(box_count)] for _ in range(box_count)]
print(current_state)

top_frame = ttk.Frame(window, height=100)
top_frame.pack()

next_button = ttk.Button(top_frame, text="Next", command=next_step)
next_button.pack()

canvas = tk.Canvas(window, bg="#181818", width=window_width, height=window_width)
canvas.pack()


def callback(event):
    scale = box_count / window_width
    c = math.floor(scale * event.x)
    r = math.floor(scale * event.y)
    current_state[r][c] = (current_state[r][c] + 1) % 2
    print(current_state)
    draw_current_state()


canvas.bind("<Button-1>", callback)

# draw_box(can=canvas, x=100, y=100)
current_state[0][3] = 1
draw_current_state()

window.mainloop()
