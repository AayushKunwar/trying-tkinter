"""3 types of button
button, checkbutton, radio button"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("buttons")
window.geometry("600x400")


# button
def button_func():
    print("a basic function")
    print(radio_var.get())
    print(button_string.set("changed"))


button_string = tk.StringVar(value="button with string var")

button = ttk.Button(
    master=window,
    text="a simple button",
    command=button_func,
    textvariable=button_string,
)
button.pack()

# check button
# check_var = tk.StringVar()
check_var = tk.IntVar()
# check_var = tk.BooleanVar()
check1 = ttk.Checkbutton(
    master=window,
    text="check button",
    command=lambda: print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5,
)
check1.pack()
# it dont have .get method

check2 = ttk.Checkbutton(
    window, text="check2 button", command=lambda: print("check button 2")
)
check2.pack()

# radio buttons
# only one button is ever activated
# they MUST have a value
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text="radio1",
    value="radio1",
    variable=radio_var,
    command=lambda: print(radio_var.get()),
)
radio1.pack()
radio2 = ttk.Radiobutton(window, text="radio2", value=2, variable=radio_var)
radio2.pack()

exer_var = tk.StringVar()
exer_bool = tk.BooleanVar()


def exer_radio_func():
    print(exer_var.get())
    exer_bool.set(False)


check3 = ttk.Checkbutton(
    master=window,
    text="exercise check",
    variable=exer_bool,
    command=lambda: print(exer_var.get()),
)
check3.pack()
radio3 = ttk.Radiobutton(
    master=window,
    text="exercise radio1",
    value="a",
    variable=exer_var,
    command=exer_radio_func,
)
radio3.pack()
radio4 = ttk.Radiobutton(
    master=window,
    text="exercise radio2",
    value="b",
    variable=exer_var,
    command=exer_radio_func,
)
radio4.pack()


window.mainloop()
