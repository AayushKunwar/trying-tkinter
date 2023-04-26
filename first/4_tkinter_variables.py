"""tkinter variables, 
automatically updated by widgets
used to update widgets (widgets interact with eachother)

store only basic data"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("tkinter variable")


def button_func():
    print(string_var.get())
    string_var.set("button pressed")


# tkinter variable
string_var = tk.StringVar(value="start value")
# IntVar, DoubleVar, BooleanVar

label = ttk.Label(master=window, text="some text", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

window.mainloop()
