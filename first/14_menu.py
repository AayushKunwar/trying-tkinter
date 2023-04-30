import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Tk menu")

# Nested menu possible
# menu
menu = tk.Menu(window)

# submenu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="new", command=lambda: print("new file"))
file_menu.add_separator()
file_menu.add_command(label="open", command=lambda: print("open file"))
menu.add_cascade(label="file", menu=file_menu)
# checkout online for more options

# another sub menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(
    label="help entry", command=lambda: print(help_check_string.get())
)

help_check_string = tk.StringVar()
help_menu.add_checkbutton(
    label="chekc", onvalue="on", offvalue="off", variable=help_check_string
)

menu.add_cascade(label="help", menu=help_menu)

window.configure(menu=menu)

# https://www.tutorialspoint.com/python/tk_menu.htm
# menu button
menu_button = ttk.Menubutton(window, text="menu button")
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label="entry 1", command=lambda: print("test1"))
button_sub_menu.add_checkbutton(label="check1")
menu_button.configure(menu=button_sub_menu)

window.mainloop()
