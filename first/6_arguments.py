import tkinter as tk
from tkinter import ttk


def button_func(entry_string):
    print("a button was pressed")
    print(entry_string.get())


def outer_func(parameter):
    def inner_func():
        print("a button was pressed")
        print(parameter.get())

    return inner_func


window = tk.Tk()
window.title("buttons, functions and arguments")
window.geometry("500x400")

entry_string = tk.StringVar(value="test")
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text="button", command=outer_func(entry_string))
button.pack()

# just use this
# command=lambda: button_func(entry_string)
window.mainloop()
