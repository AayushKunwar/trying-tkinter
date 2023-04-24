# tk widgets are original old ones
# ttk widgets are newer modern looking ones

import tkinter as tk
from tkinter import ttk


def button_func():
    print("a button was pressed")


def print_hello():
    print("Hello")


# create a window
# can be named root or app
window = tk.Tk()
window.title("Window and widgets")
window.geometry("800x500")

# create widgets

# ttk widgets
label = ttk.Label(master=window, text="this is some text")
label.pack()

# tk widgets
# this accepts multiline input
text = tk.Text(master=window)
text.pack()

# ttk entry (single line i think)
entry = ttk.Entry(master=window)
entry.pack()

# video exercise (ignore this lines)
ttk.Label(master=window, text="my label").pack()
ttk.Button(master=window, text="print hello", command=print_hello).pack()

# ttk button
button = ttk.Button(master=window, text="a button", command=button_func)
button.pack()
# run
window.mainloop()
"""mainloop
1. updates gui
2. checks for events(button clicks, mouse movement, closing window

everything below mainloop line works after the window is closed)"""
