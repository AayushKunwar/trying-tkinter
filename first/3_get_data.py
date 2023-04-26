import tkinter as tk
from tkinter import ttk


def button_func():
    # lots of widgets dont have get attribute
    # print(label.get())
    entry_text = entry.get()

    # update the label
    # label.config(text="some other text")
    # label.configure(...)
    # use configure method (modern??)
    label["text"] = entry_text
    # some other attributes
    entry["state"] = "disabled"

    # to print all attributes
    # print(label.configure())


def button_exer():
    label["text"] = "some text"
    entry["state"] = "enabled"


# windows
window = tk.Tk()
window.title("Getting and setting widgets")

# widgets
label = ttk.Label(master=window, text="wasssso")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="click me", command=button_func)
button.pack()

button2 = ttk.Button(master=window, text="exercise", command=button_exer)
button2.pack()
# buttons have config method to change them
# Lable.config(text="some text")
# Label["text"] = "some new text"
# run
window.mainloop()
